import subprocess
from Platform import *

def install(program):
	if "Ubuntu" in getDistro():
		call("sudo apt-get install " + program)
	else:
		notSupported()
def addRepository(repo):
	if "Ubuntu" in getDistro():
		call("sudo add-apt-repository " + repo)
	else:
		notSupported()
def update():
	if "Ubuntu" in getDistro():
		call("sudo apt-get update")
	else:
		notSupported()
def call(command):
	subprocess.call(command, shell=True)
