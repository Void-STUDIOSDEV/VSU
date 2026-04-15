import time
sleep = time.sleep
#required modules and definitions


sleep(0.5); print("Text Interface Calculator, TIC")
sleep(0.5); print("Version 01.00.01")
sleep(0.5); print("COPYRIGHT VOID STUDIOS, VOID STUDIOS SOURCE PROGRAM 2025-2026")
sleep(0.5); print("GNU General Public License 2.x")
sleep(0.5); print("Reconstruction of Py-Calculator")
#introduction


while True:
	sleep(0.5); print("\n\nADDITION [+], MULTIPLICATIONS [X], DIVISION [/], SUBTRACTION [-], POWER [^], REMAINDER [*], PERCENT OF [%], PERCENT SOMETHING IS [>], EXIT [E]")
	c = input("INPUT: ").upper()
	#Allows user input
	
	if c == "E":
		sleep(0.5); print("Goodbye!")
		break
		
	elif c == "+":
		a = float(input("\nENTER NUMBER: "))
		b = float(input("ENTER SECOND: "))
		total = a + b
		print(f"TOTAL: {total}")
		
	elif c == "X":
		a = float(input("\nENTER NUMBER: "))
		b = float(input("ENTER SECOND: "))
		total = a * b
		print(f"TOTAL: {total}")
		
	elif c == "/":
		a = float(input("\nENTER NUMBER: "))
		b = float(input("ENTER SECOND: "))
		total = a / b
		print(f"TOTAL: {total}")
	
	elif c == "-":
		a = float(input("\nENTER NUMBER: "))
		b = float(input("ENTER SECOND: "))
		
		if b == 0:
			if a == 0:
				print("TOTAL: Indeterminate")
			else:
				print("TOTAL: Undefined")
		
		else:
			total = a / b
			print(f"TOTAL: {total}")
		
		print(f"TOTAL: {total}")
		
	elif c == "^":
		base = float(input("\nENTER NUMBER: "))
		exponent = float(input("ENTER SECOND: "))
		total = base ** exponent
		print(f"TOTAL: {total}")
		
	elif c == "*":
		a = float(input("\nENTER NUMBER: "))
		b = float(input("ENTER SECOND: "))
		total = a % b
		print(f"TOTAL: {total}")
		
	elif c == "%":
		percent = float(input("\nENTER NUMBER: "))
		num = float(input("ENTER SECOND: "))
		total = (percent / 100) * num
		print(f"TOTAL: {total}")
		
	elif c == ">":
		num = float(input("\nENTER NUMBER: "))
		total = float(input("ENTER SECOND: "))
		percent = (num / total) * 100
		print(f"{num} is {percent}% of {total}")
		
	elif c not in ["+", "X", "/", "-", "^", "*", "%", ">"]:
		print("NOT A VALID INPUT.\n")
		
		
#Use this to find words:
#!!SEARCH FUNCTION DOES NOT WORK IN TERMINAL-BASED EDITORS NOR GEANY!!
