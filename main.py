from library import add_book, remove_book, search_book, add_user, issue_book, return_book

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Add User")
        print("5. Issue Book")
        print("6. Return Book")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
            print("Book added successfully!")
        elif choice == '2':
            book_id = int(input("Enter book ID to remove: "))
            remove_book(book_id)
            print("Book removed successfully!")
        elif choice == '3':
            title = input("Enter book title to search: ")
            results = search_book(title)
            for book in results:
                print(book)
        elif choice == '4':
            name = input("Enter user name: ")
            add_user(name)
            print("User added successfully!")
        elif choice == '5':
            book_id = int(input("Enter book ID to issue: "))
            user_id = int(input("Enter user ID: "))
            issue_book(book_id, user_id)
            print("Book issued successfully!")
        elif choice == '6':
            book_id = int(input("Enter book ID to return: "))
            user_id = int(input("Enter user ID: "))
            return_book(book_id, user_id)
            print("Book returned successfully!")
        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
    