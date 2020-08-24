 #import pyttsx3
import os

# pysttx3.speak("welcome to my tools", end='')


while True :

	print(" chat with me with your requirements : " , end=' ' )
	p=input()
	# print(p)
	# os.system(p)
	
	if (("run" in p) or ("open" in p)) and ("chrome" in p) and ("don't" not in p): 
		os.system("chrome")
	
	elif (("run" in p) or ("open" in p)) and ("whatsapp" in p) and ("don't" not in p):
		os.system("chrome  web.whatsapp.com")

	elif (("run" in p) or ("open" in p)) and ("google meet" in p) and ("don't" not in p):
		os.system("chrome  meet.google.com")

	elif (("run" in p) or ("open" in p)) and ("gmail" in p) and ("don't" not in p):
	  	os.system("chrome  mail.google.com")

	elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)) and ("don't" not in p):
		os.system("notepad")

	elif (("run" in p) or ("open" in p)) and ("zoom" in p) and ("don't" not in p) :
		os.system("zoom")

	elif (("run" in p) or ("open" in p)) and ("vlc" in p) and ("don't" not in p) :
		os.system("vlc")
	
	elif (("run" in p) or ("open" in p)) and ("virtualbox" in p)  and ("don't" not in p) :
		os.system("virtualbox")


	elif  ("exit" in p)  or ("quit" in p) and ("don't" not in p) :
		  break

	else:
		  print("  don't support")
