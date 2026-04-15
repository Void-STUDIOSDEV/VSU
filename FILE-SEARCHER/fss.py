import os
import time
import sys
sleep = time.sleep
#required modules

sleep(0.5); print("File Size Search, FSS")
sleep(0.5); print("PART OF VOID STUDIOS UTILITY SET")
sleep(0.5); print("COPYRIGHT VOID STUDIOS 2026")
sleep(0.5); print("GNU General Public License 2.x")
sleep(0.5); print("CLICK E TO EXIT, S TO LIST")

home = os.path.expanduser("~")

files = []

while True:
	choice = input("CHOICE: ").upper()
	
	if choice == "E":
		sleep(0.5); print("Goodbye:")
		break
		
	if choice == "S":
		sleep(0.5); print("\nLISTING...\n\n")
		for root, _, fs in os.walk(home):
			for f in fs:
				p = os.path.join(root, f)
				try:
					s = os.path.getsize(p)
					files.append((s, p))
				except:
					pass
			
		files.sort(reverse=True)
	
		for s, p in files[:20]:
			sleep(1); print(round(s/1024**3, 2), "GB", p) #adjust the sleep time, files will either appear faster or slower
			
	if choice not in ["E", "S"]:
		print("INVALID.\n")
		continue
