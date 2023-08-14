# Create a program that can be used by a bookstore clerk.
# import modules
import sqlite3
import pandas as pan
import sys

#####################################################################################################

# define an exception for a book that was not found
class NoIdException(Exception):
    "Raised when the id is not in books"
    pass

# define an exception for when a new book id does not meet the requirements
class InvalidIdException(Exception):
    "Raised when the id is not 4 characters in length"
    pass

# The program should allow the clerk to perform various tasks:        
# ○ add new books to the database
# request the user to input the required fields for the new record
# insert record into books
# use .commit on db object (not cursor) to save changes to the database
# print out the updated table
def enter_book():
    print('Please enter the information for the new book entry')
    new_id = int(input("Enter the book's id:\t"))
    new_title = input("Enter the book's title:\t")
    new_author = input("Enter the book's author :\t")
    new_qty = int(input("Enter the quantity of books:\t"))

    cursor.execute('''INSERT OR REPLACE INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', (new_id,new_title,new_author,new_qty))                     
    print('The new book was entered.')

    db.commit()          

    # use pandas to print table (pip install pandas in cmd after cd to pip file path)   
    print(pan.read_sql('SELECT * FROM books', db))
    print()

# ○ update book information
# use which_bk as a parameter in the function
# use a while loop to display a menu of fields to the user with if-elif-else statements
# request the user to input the field to update
# use try-except block as defense for undesirable input
# use .commit on db object (not cursor) to save changes to the database
# print out the updated record
def update_book(which_bk):
    while which_bk != 0:                  
        which_field = int(input('''Enter the number for the field you want to update:
0 exit update
1 id
2 Title
3 Author
4 Qty
'''))
        if which_field == 0:
            print('You have left the update.')
            print()
            break

        elif which_field == 1:            
            try:
                update_id = int(input('Enter the new id for the book:\t'))
                # cast back to str to use len()
                if len(str(update_id)) != 4:
                    raise InvalidIdException
                else:
                    print(f'The new id {update_id} was received')
                cursor.execute('''UPDATE books SET id = ? WHERE id = ?''', (update_id, which_bk))                                              
                db.commit()
                cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE id = ?''', (update_id,))
                book_record = cursor.fetchone()
                print(f'The book id was updated.\n{book_record}')
                print()
                    
            except InvalidIdException:
                print('The id requires 4 integers. Please try again.')
                print()

            finally:
                db.close()

        elif which_field == 2:
            update_title = input('Enter the new title for the book:\t')
            cursor.execute('''UPDATE books SET Title = ? WHERE id = ?''', (update_title, which_bk))
            db.commit()
            cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE id = ?''', (which_bk,))
            book_record = cursor.fetchone()
            print(f'The book title was updated.\n{book_record}')
            print()

        elif which_field == 3:
            update_author = input('Enter the new author for the book:\t')
            cursor.execute('''UPDATE books SET Author = ? WHERE id = ?''', (update_author, which_bk))
            db.commit()
            cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE id = ?''', (which_bk,))
            book_record = cursor.fetchone()
            print(f"The book's author was updated.\n{book_record}")
            print()

        elif which_field == 4:
            update_qty = int(input('Enter the new quantity for the book:\t'))
            cursor.execute('''UPDATE books SET Qty = ? WHERE id = ?''', (update_qty, which_bk))
            db.commit()
            cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE id = ?''', (which_bk,))
            book_record = cursor.fetchone()
            print(f"The book's quantity was updated.\n{book_record}")
            print()

        else:
            print('Invalid selection. Please Try again.\n')
            
# ○ delete books from the database
# delete the book chosen from the search_books()
# use .commit to save changes to the database
# check that the book is no longer in the database
# print out a confirmation statement
def delete_book(which_bk):    
    cursor.execute('''DELETE FROM books WHERE id = ?''', (which_bk,))    
    db.commit()
    cursor.execute('''SELECT id, Title FROM books WHERE id = ?''', (which_bk,))
    check_id = cursor.fetchone()
    if check_id is None:
        print('The deletion was successful.\n')
    
# ○ search the database to find a specific book.
# use a while loop with a try-except block to search for valid book records
# print out an error statement for incorrect ids and print the book that was found
# return the book id the user enters to use as a parameter for other functions
def search_books():
    while True:
        try:
            which_bk = int(input('\nEnter the id of the book:\t'))
            # do a check to see if valid id
            cursor.execute('''SELECT id, Title FROM books WHERE id = ?''', (which_bk,))
            check_id = cursor.fetchone()
            if check_id is None:
                raise NoIdException
            else:
                print(f"The book was located.\n{check_id}")
                print()
                break

        except NoIdException:
            print('There is no book with that id. Please try again.')
            print()

    return which_bk           

#####################################################################################################
        
#● Create a database called ebookstore  
# connect to the database
# pass the name of the database file to open or create it
db = sqlite3.connect('ebookstore')

# get a cursor object to execute SQL statements and alter the database
cursor = db.cursor()

# Create a a table called books.
# use IF NOT EXISTS to avoid sqlite3.OperationalError: table books already exists
# make id the primary key
cursor.execute('''
CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
''')

# use .commit on db object (not cursor) to save changes to the database
db.commit()

# The table should have the following structure:
# fields:   id, Title, Author, Qty
# ● Populate the table with the following values.
# You can also add your own values if you wish.
# 3001 A Tale of Two Cities Charles Dickens 30
# 3002 Harry Potter and the Philosopher's Stone J.K. Rowling 40
# 3003 The Lion, the Witch and the Wardrobe C. S. Lewis 25
# 3004 The Lord of the Rings J.R.R Tolkien 37
# 3005 Alice in Wonderland Lewis Carroll 12
# assign variables for each entry
id1 = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30

id2 = 3002
title2 = "Harry Potter and the Philosopher's Stone"
author2 = 'J.K. Rowling'
qty2 = 40

id3 = 3003
title3 = 'The Lion, the Witch and the Wardrobe'
author3 = 'C. S. Lewis'
qty3 = 25

id4 = 3004
title4 = 'The Lord of the Rings'
author4 = 'J.R.R Tolkien'
qty4 = 37

id5 = 3005
title5 = 'Alice in Wonderland'
author5 = 'Lewis Carroll'
qty5 = 12

# create a list of the records to insert later
library = [(id1,title1,author1,qty1), (id2,title2,author2,qty2),
           (id3,title3,author3,qty3), (id4,title4,author4,qty4),
           (id5,title5,author5,qty5)]

# use INSERT OR REPLACE to avoid sqlite3.IntegrityError: UNIQUE constraint failed: books.id
cursor.executemany('''INSERT OR REPLACE INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', library)

# use .commit to save changes to the database
db.commit()

# The program should perform the function that the user selects.
# print out a welcome statement
print('Welcome to the bookshelf editor. Here is the current bookshelf:\n')

# use pandas to print table (pip install pandas in cmd after cd to pip file path)   
print(pan.read_sql('SELECT * FROM books', db))
print()

# the program should present the user with a menu
# use a boolean while loop to display the menu with if-elif-else statements
# request the user to input an option from the menu
while True:
    menu = int(input('''Enter a number from the menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
:
'''))

    if menu == 0:
        print('Goodbye!')
        # use sys.exit() to prevent another loop if quitting & exit the program
        import sys
        sys.exit()

    elif menu == 1:
        enter_book()

    elif menu == 2:
        update_book(search_books())

    elif menu == 3:
        delete_book(search_books())

    elif menu == 4:
        search_books()

    else:
        print("Invalid selection. Please Try again.\n")

# close the connection to db
db.close()

