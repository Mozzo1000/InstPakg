import subprocess
from Platform import *

def install(program):
	if getPackage("apt"):
		call("sudo apt-get install " + program)
	elif getPackage("yum"):
		call("sudo yum install " + program)
	else:
		notSupported()
def addRepository(repo):
	if getPackage("apt"):
		call("sudo add-apt-repository " + repo)
	elif getPackage("yum"):
		call("sudo yum-config-manager --add-repo " + repo)
	else:
		notSupported()
def update():
	if getPackage("apt"):
		call("sudo apt-get update")
	if getPackage("yum"):
		pass
	else:
		notSupported()
def call(command):
	subprocess.call(command, shell=True)
