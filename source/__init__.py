import json, subprocess, os, glob, GlobalUtils
from JsonUtil import *
from menu import cmenu
yes = set(["yes", "y"])
home = os.getenv("HOME")
JSON_LOCATION = home + "/.instpakg"
DEFAULT_JSON = JSON_LOCATION + "/DEFAULT.json"
jsonInstall = ""
markedInstall = []
markedRepo = []

def initJson():
	global jsonInstall
	load_json(DEFAULT_JSON)
	jsonInstall = get_json("install")

def bulkInstall():
	initJson()
	for item in jsonInstall:
		subprocess.call("sudo add-apt-repository " + item["repo"] + " -y", shell=True)
	subprocess.call("sudo apt-get update", shell=True)
	for item in root:
		if item["command"]:
			subprocess.call(item["command"], shell=True)
		subprocess.call("sudo apt-get install -y " + item["app"], shell=True)
	close_json()

"""def aptInstall(program, repo, command):
	global yes
	if not repo and not command:
		subprocess.call("sudo apt-get install " + program, shell=True)
	elif repo:
		choice = raw_input("Do you want to add ppa " + repo + " (Required to install " + program +") (y/n)").lower()
		if choice in yes:
			subprocess.call("sudo add-apt-repository " + repo + " && sudo apt-get update", shell=True)
			subprocess.call("sudo apt-get install " + program, shell=True)
		else:
			print("Cancelled install of " + program)
	elif command:
		subprocess.call(command, shell=True)
		subprocess.call("sudo apt-get update && sudo apt-get install " + program, shell=True)
"""

def aptInstall(program, repo, command):
	global yes
	markedInstall.append(program)

def promptInstall():
	GlobalUtils.clear()
	initJson()
	for item in jsonInstall:
		print(item["app"] + "\n-----------------\nINSERT DESCRIPTION!\n")
		
		choice = raw_input("Do you want to mark\033[1m " + item["app"] + "\033[0m for install? (y/n)").lower()
		if choice in yes:
			aptInstall(item["app"], item["repo"], item["command"])

	choice = raw_input("Are you sure you want to install the following programs? - " + str(markedInstall))
	if choice in yes:
		for item in markedInstall:
			subprocess.call("sudo apt-get install " + item, shell=True)
		print("Installing EVERYTHING!")
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





