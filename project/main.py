from app import *

print("-"*10, "WELCOME TO MY_BOOKS", "-"*20)
print("\n")

while True:
	list_users()
	print("A.Add user\nE.Exit")
	print("-----Select-----")

	select = input("-->")

	if select == "A" or select == "a":
		add_user()

	elif select == "E" or select == "e":
		print("\nThank you!!")
		exit()

	else:
		while True:
			print("What would you like to do ?")
			print("\n1.MY TBR\n2.My Shelf\n3.Favourites\n4.Suggestions\n5.Exit to Menu\n")

			ch = input("---->")
			select = int(select)


			if ch == "1":
				see_tbr(select)
			elif ch == "2":
				see_read(select)
			elif ch == "3":
				see_fav(select)
			elif ch == "4":
				see_suggestions(select)
			else:
				break



