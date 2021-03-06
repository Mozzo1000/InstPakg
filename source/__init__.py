import subprocess, os, glob, GlobalUtils, InstallUtil, Platform
from JsonUtil import *
from menu import cmenu
yes = set(["yes", "y"])
home = os.getenv("HOME")
JSON_LOCATION = home + "/.instpakg"
DEFAULT_JSON = JSON_LOCATION + "/DEFAULT.json"
jsonInstall = ""

markedInstall = []
markedRepo = []
markedCommand = []

def initJson():
	global jsonInstall
	load_json(DEFAULT_JSON)
	if Platform.getPackage("apt"):
		jsonInstall = get_json("apt")
	elif Platform.getPackage("yum"):
		jsonInstall = get_json("yum")

def bulkInstall():
	initJson()
	for item in jsonInstall:
		InstallUtil.forceAddRepository(item["repo"])
	InstallUtil.update()
	for item in root:
		if item["command"]:
			InstallUtil.call(item["command"])
		InstallUtil.forceInstall(item["app"])
	close_json()

def mark(program, repo, command):
	markedInstall.append(program)
	if repo:
		choice = raw_input("Do you want to add ppa " + repo + " (Required to install " + program +") (y/n)").lower()
		if choice in yes:
			markedRepo.append(repo)
		else:
			print("Cancelled install of " + program)
			markedInstall.remove(program)
	elif command:
		choice = raw_input("The following command is required in order to install " + program + "are you sure? (y/n)\n\033[1m" + command + "\033[0m").lower()
		if choice in yes:
			markedCommand.append(command)
		else:
			print("Cancelled install of " + program)
			markedInstall.remove(program)
		
def promptInstall():
	GlobalUtils.clear()
	initJson()
	for item in jsonInstall:
		print(item["app"] + "\n-----------------\nINSERT DESCRIPTION!\n")
		
		choice = raw_input("Do you want to mark\033[1m " + item["app"] + "\033[0m for install? (y/n)").lower()
		if choice in yes:
			mark(item["app"], item["repo"], item["command"])
	if markedCommand:
		choice = raw_input("The following code will now run, are you sure (y/n) \n" + str(markedCommand)).lower()
		if choice in yes:
			for item in markedCommand:
				InstallUtil.call(item)
	if markedRepo:
		choice = raw_input("The following repositories will be added, are you sure? (y/n)\n\033[1m" + str(markedRepo) + "\033[0m").lower()
		if choice in yes:
			for item in markedRepo:
				InstallUtil.addRepository(item)
			InstallUtil.update()
	else:
		print("No external repositories are required!")
	choice = raw_input("Are you sure you want to install the following programs? -\n " + str(markedInstall))
	if choice in yes:
		for item in markedInstall:
			InstallUtil.install(item)
	close_json()

def selectJSON():
	global DEFAULT_JSON
	num = -1
	GlobalUtils.clear()
	for file in os.listdir(JSON_LOCATION):
		if file.endswith(".json"):
			files = glob.glob(JSON_LOCATION+"/*.json")
			num += 1
			print("["+str(num) + "] " + file)
	choice = raw_input("Choose one [0-"+str(num)+"] ")
	print(files[int(choice)])
	DEFAULT_JSON = files[int(choice)]
	
def main():
	try:
		list = [{ "Install software": promptInstall }, {"Bulk Software Install": bulkInstall}, {"Select JSON file": selectJSON}, {"Exit": GlobalUtils.exit}]
		menu = cmenu(list, "InstPakg Menu")
		menu.display()
	except SystemExit:
		pass
	else:
		menu.cleanup()





