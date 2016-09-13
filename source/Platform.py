import platform, time, os

def getDistro(pos = 0):
	return platform.linux_distribution()[pos]
def getOS():
	return platform.system()
def getKernel():
	return platform.release()
def notSupported():
	print("Your package manager is not supported\nList of supported package managers\nDpkg - Apt\nRPM - Yum\nRPM - DNF")
	time.sleep(1)
def getPackage(package):
	path = "/usr/bin/" + package
	if os.path.exists(path):
		return True
