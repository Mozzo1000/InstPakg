import subprocess
from Platform import *

def install(program):
	if getPackage("apt"):
		call("sudo apt-get install " + program)
	elif getPackage("yum"):
		call("sudo yum install " + program)
	elif getPackage("dnf"):
		call("sudo dnf install " + program)
	else:
		notSupported()
def addRepository(repo):
	if getPackage("apt"):
		call("sudo add-apt-repository " + repo)
	elif getPackage("yum"):
		call("sudo yum-config-manager --add-repo " + repo)
	elif getPackage("dnf"):
		call("sudo dnf ¨config-manager --add-repo " + repo)
	else:
		notSupported()
def update():
	if getPackage("apt"):
		call("sudo apt-get update")
	if getPackage("yum"): #Side note, I should really test to see if yum and dnf needs to "update"
		pass
	if getPackage("dnf"):
		pass
	else:
		notSupported()
def call(command):
	subprocess.call(command, shell=True)

def forceInstall(program):
	if getPackage("apt"):
		call("sudo apt-get install -y " + program)
	elif getPackage("yum"):
		call("sudo yum -y install " + program)
	elif getPackage("dnf"):
		call("sudo dnf -y install " + program)
	else:
		notSupported()
def forceAddRepository(repo):
	if getPackage("apt"):
		call("sudo add-apt-repository -y " + repo)
	elif getPackage("yum"):
		call("sudo yum-config-manager --add-repo " + repo)
	elif getPackage("dnf"):
		call("sudo dnf config-manager --add-repo " + repo)
	else:
		notSupported()
