from models import *
from tabulate import tabulate

db.connect()

'''
rem_fav
check_fav
see_fav
check_read
see_read
list_by_genre
list_by_author
list_by_year
see_suggestions
check_sugg
'''

def check_user():
	users = User.select()
	if len(users)==0:
		return 0
	else:
		return 1

def list_users():
	yes = check_user()
	if yes:
		user_list = []
		users = User.select()
		for user in users:
			user_list.append([user.id, user.name])

		headers = ["ID", "Username"]
		print(tabulate(user_list, headers, tablefmt = "fancy_grid"))


	else:
		print("\nNO USERS!!!!")
		print("ADD USER!!!!\n")

def add_user():
	name = input("Enter username: ")

	user = User(name=name)
	user.save()

def check_tbr(select):
	tbrs = Book.select().where(Book.owner_id == select , Book.is_read == False)

	if len(tbrs)==0:
		return 0
	else:
		return 1

def see_tbr(select):
	yes = check_tbr(select)
	if yes:

		tbrs = Book.select().where(Book.owner_id == select, Book.is_read == False)

		tbr_list = []
		for tbr in tbrs:
			tbr_list.append([tbr.id, tbr.name, tbr.author, tbr.genre])

		headers = ["ID", "Name", "Author", "Genre"]
		print(tabulate(tbr_list, headers, tablefmt = "fancy_grid"))

		print("1.Add a book\n\
2.Mark as done\n\
3.Back")

		choice = int(input("--->"))

		if choice == 1:
			add_book(select)
		elif choice == 2:
			mark_as_done(select)
		else:
			return

	else:
		print("\nNO BOOKS IN YOUR TBR!")
		print("1.Add a book\n2.Back\n")

		choice = int(input("--->"))

		if choice == 1:
			add_book(select)
		else:
			return

def add_book(select):
	name = input("Name of the Book: ")
	author = input("Name of author: ")
	genre = input("Genre:  ")

	book = Book(name = name, author = author, genre = genre, owner = select, is_read = False, is_fav = False)
	book.save()

def mark_as_done(select):
	choice = input("Enter book ID :  ")

	year = int(input("Enter year : "))
	rating = float(input("Rate ?/5 : "))
	addfav = input("Add to favorites? [y/n]: ")

	if addfav == "y":
		book =  Book.update(is_read = True, rating = rating, year = year, is_fav=True).where(Book.owner_id == select ,Book.is_read == False , Book.id == choice).execute()

	else:
		book =  Book.update(is_read = True, rating = rating, year = year).where(Book.owner_id == select , Book.is_read == False , Book.id == choice).execute()

	
def check_fav(select):
	books = Book.select().where(Book.owner_id == select, Book.is_fav == True)

	if len(books)==0:
		return 0
	else:
		return 1

def see_fav(select):
	yes = check_fav(select)
	if yes:

		favs = Book.select().where(Book.owner_id == select, Book.is_fav == True)

		fav_list = []
		for fav in favs:
			fav_list.append([fav.id, fav.name, fav.author, fav.genre])

		headers = ["ID", "Name", "Author", "Genre"]
		print(tabulate(fav_list, headers, tablefmt = "fancy_grid"))
		print("1\n.Remove favorite\n2.Back")

		ch = int(input("--->"))

		if ch == 1:
			which_book = input("Choose book id: ")
			book =  Book.update(is_fav=False).where(Book.owner_id == select , Book.id == ch).execute()

		else:
			return

	else:
		print("No books in favourties")

def check_read(select):
	books = Book.select().where(Book.owner_id == select, Book.is_read== True)

	if len(books)==0:
		return 0
	else:
		return 1

def see_read(select):
	yes = check_read(select)
	if yes:

		reads = Book.select().where(Book.owner_id == select , Book.is_read == True)

		read_list = []
		for read in reads:
			read_list.append([read.id, read.name, read.author, read.genre, read.year, read.rating])

		headers = ["ID", "Name", "Author", "Genre", "Year", "Rating"]
		print(tabulate(read_list, headers, tablefmt = "fancy_grid"))

def check_suggestions(select):
	sugg = Book.select().where(Book.owner_id != select, Book.is_fav == True)

	if len(sugg)==0:
		return 0
	else:
		return 1

def see_suggestions(select):
	yes = check_suggestions(select)
	if yes:

		suggs = Book.select().where(Book.owner_id != select ,Book.is_fav == True)

		sugg_list = []
		for sugg in suggs:
			sugg_list.append([sugg.id, sugg.name, sugg.author, sugg.genre])

		headers = ["ID", "Name", "Author", "Genre"]
		print(tabulate(sugg_list, headers, tablefmt = "fancy_grid"))

	else:
		print("\nNo books in suggestions")





















 



















