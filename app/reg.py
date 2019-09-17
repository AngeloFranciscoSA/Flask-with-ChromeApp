import winreg

def get_chrome_path():
	kpath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
	rk = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, kpath)

	i = 0
	while True:	
		try:
			k, v, idx = winreg.EnumValue(rk, i)
			if k == '': 
				return v

		except OSError:
			return ""

		i += 1
		

if __name__=="__main__":
	print(get_chrome_path())