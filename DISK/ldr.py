import shutil
import time
import sys
sleep = time.sleep
def disk_size():
		sleep(0.7); print("LISTING...")
		total, used, free = shutil.disk_usage(".")
		sleep(0.5); print("TOTAL: ", total / (1024**3), "GB")
		sleep(0.5); print("USED: ", used / (1024**3), "GB")
		sleep(0.5); print("FREE: ", free / (1024**3), "GB\n")
#required modules


sleep(0.5); print("\nLinux Disk Reader, LDR")
sleep(0.5); print("Version 01.00.00")
sleep(0.5); print("COPYRIGHT VOID STUDIOS 2026")
sleep(0.5); print("COVERED UNDER GNU General Public License 2.x")
sleep(0.5); print("E TO EXIT, S TO LIST [START]")
sleep(0.5); print("R TO LIST WITHOUT PROGRAM ENDING [MANUAL ENDING]")
#introduction


while True:
	choice = input("CHOICE: ").upper()
	if choice == "E":
		print("Goodbye!\n")
		break
	#allows the user to exit
		
	if choice == "S":
		disk_size()
		break
	#prints out disk informations and automatically ends	
		
	if choice == "R":
		disk_size()
		continue
	#prints out disk informations. manual ending required
		
	if choice not in ["E", "S", "R"]:
		print("INVALID\n")
		continue
	#invalid input handling
