print("Selecet Menu Options by 1,2,3 or 4 to quit \n")
while True:
	menu = input("Enter a Menu Option : ")
	try:
		menu = int(menu)
		if menu == 1 or menu == 2 or menu == 3:
			print(menu," selected")
		elif menu == 4:
			print("Quit Selected")
			break;
		else:
			print("Option not recognize")
	except Exception:
		print("Enter Integer")
	
