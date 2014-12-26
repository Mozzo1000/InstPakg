import json, subprocess, curses, sys, os, glob
from menu import cmenu
yes = set(["yes", "y"])
DEFAULT_JSON = subprocess.call("wget ----", shell=True)
JSON_LOCATION = ""

def bulkInstall():
	json_data = open(DEFAULT_JSON)
	data = json.load(json_data)
	root = data["install"]
	for item in root:
		subprocess.call("sudo add-apt-repository " + item["repo"] + " -y", shell=True)
	subprocess.call("sudo apt-get update", shell=True)
	for item in root:
		if item["command"]:
			subprocess.call(item["command"], shell=True)
		subprocess.call("sudo apt-get install -y " + item["app"], shell=True) 

def aptInstall(program, repo, command):
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

def promptInstall():
	clear()
	json_data = open(DEFAULT_JSON)
	data = json.load(json_data)
	root = data["install"]
	for item in root:
		choice = raw_input("Do you want to install " + item["app"] + " (y/n)").lower()
		if choice in yes:
			aptInstall(item["app"], item["repo"], item["command"])
	json_data.close()

def exit():
	#clear()
	sys.exit(1)
def clear():
	subprocess.call("clear", shell=True)

def selectJSON():
	global DEFAULT_JSON
	num = -1
	clear()
	for file in os.listdir(JSON_LOCATION):
		if file.endswith(".json"):
			files = glob.glob(JSON_LOCATION+"/*.json")
			num += 1
			print("["+str(num) + "] " + file)
	choice = raw_input("Choose one [0-"+str(num)+"] ")
	print(files[int(choice)])
	DEFAULT_JSON = files[int(choice)]
	

def main():
	home = os.getenv("HOME")
	if not os.path.exists(home + "/.instpakg"):
		os.makedirs(home + "/.instpakg")
		global JSON_LOCATION
		JSON_LOCATION = home + "/.instpakg"
		print(JSON_LOCATION + "  "+ DEFAULT_JSON)
		subprocess.call("cp " + DEFAULT_JSON + " " + JSON_LOCATION, shell=True)
	else:
		global JSON_LOCATION
		JSON_LOCATION = home + "/.instpakg"
	try:
		list = [{ "Install software": promptInstall }, {"Bulk Software Install": bulkInstall}, {"Select JSON file": selectJSON}, {"Exit": exit}]
		menu = cmenu(list, "InstPakg Menu")
		menu.display()
	except SystemExit:
		pass
	else:
		menu.cleanup()





