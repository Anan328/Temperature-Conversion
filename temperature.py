while True:
	try:
		choice=int(input("Enter 0 for celsius to fahrenheit conversion or 1 for vice versa: "))
		print()
		if choice==0 or choice==1:
			if choice==0:
				c=float(input("Enter temp in celsius: "))
				print()
				f=((9/5)*c)+32
				f=round(f,3)
				print("Temp in fahrenheit is: ",f)
				print()
			else:
				f=float(input("Enter temp in fahrenheit: "))
				print()
				c=(f-32)*(5/9)
				c=round(c,3)
				print("Temp in celsius is: ",c)
				print()
	except Exception:
		print("Try again")
		print()