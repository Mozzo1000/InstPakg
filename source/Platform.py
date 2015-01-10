import platform, time

def getDistro(pos = 0):
	return platform.linux_distribution()[pos]
def getOS():
	return platform.system()
def getKernel():
	return platform.release()
def notSupported():
	print(getDistro() + " is not supported!")
	time.sleep(3)
