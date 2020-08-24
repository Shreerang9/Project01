 #import pyttsx3
import subprocess

# pysttx3.speak("welcome to my tools", end='')


while True :

	print(" chat with me with your requirements : " , end=' ' )
	p=input()
	# print(p)
	# subprocess.getoutput(p)
	
	if (("run" in p) or ("open" in p)) and ("chrome" in p) and ("don't" not in p):
		subprocess.getoutput(" chrome ")

	elif (("run" in p) or ("open" in p)) and ("whatsapp" in p) and ("don't" not in p):
		subprocess.getoutput("chrome  web.whatsapp.com")
	
	elif (("run" in p) or ("open" in p)) and ("youtube" in p) and ("don't" not in p):
		subprocess.getoutput("chrome  www.youtube.com")


	elif (("run" in p) or ("open" in p)) and ("google meet" in p) and ("don't" not in p):
		subprocess.getoutput("chrome  meet.google.com")

	elif (("run" in p) or ("open" in p)) and ("gmail" in p) and ("don't" not in p):
		subprocess.getoutput("chrome  mail.google.com")

	elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)) and ("don't" not in p):
		subprocess.getoutput("notepad")

	elif (("run" in p) or ("open" in p)) and ("zoom" in p)and ("don't" not in p) :
		subprocess.getoutput("zoom")

	elif (("run" in p) or ("open" in p)) and ("vlc" in p) and ("don't" not in p) :
		subprocess.getoutput("vlc")
	
	elif (("run" in p) or ("open" in p)) and ("virtualbox" in p) and ("don't" not in p):
		subprocess.getoutput("virtualbox")


	
	

	elif  ("exit" in p)  or ("quit" in p) and ("don't" not in p):
		  break

	else:
		  print("  don't support")
