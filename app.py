import tkinter as tk
from tkinter import messagebox
from library import add_book, remove_book, search_book, add_user, issue_book, return_book

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.create_widgets()

    def create_widgets(self):

         # Search Book
        self.search_book_frame = tk.LabelFrame(self.root, text="Search Book")
        self.search_book_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.search_book_label = tk.Label(self.search_book_frame, text="Title")
        self.search_book_label.grid(row=0, column=0, padx=5, pady=5)
        self.search_book_entry = tk.Entry(self.search_book_frame)
        self.search_book_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_book_button = tk.Button(self.search_book_frame, text="Search Book", command=self.search_book)
        self.search_book_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.search_results_text = tk.Text(self.search_book_frame, height=10, width=50)
        self.search_results_text.grid(row=2, column=0, columnspan=2, padx=5, pady=3)
    
        # Add Book
        self.add_book_frame = tk.LabelFrame(self.root, text="Add Book")
        self.add_book_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.book_title_label = tk.Label(self.add_book_frame, text="Title")
        self.book_title_label.grid(row=0, column=0, padx=5, pady=5)
        self.book_title_entry = tk.Entry(self.add_book_frame)
        self.book_title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.book_author_label = tk.Label(self.add_book_frame, text="Author")
        self.book_author_label.grid(row=1, column=0, padx=5, pady=5)
        self.book_author_entry = tk.Entry(self.add_book_frame)
        self.book_author_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_book_button = tk.Button(self.add_book_frame, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Add User
        self.add_user_frame = tk.LabelFrame(self.root, text="Add User")
        self.add_user_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.user_name_label = tk.Label(self.add_user_frame, text="Name")
        self.user_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.user_name_entry = tk.Entry(self.add_user_frame)
        self.user_name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.add_user_button = tk.Button(self.add_user_frame, text="Add User", command=self.add_user)
        self.add_user_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Issue Book
        self.issue_book_frame = tk.LabelFrame(self.root, text="Issue Book")
        self.issue_book_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.issue_book_id_label = tk.Label(self.issue_book_frame, text="Book ID")
        self.issue_book_id_label.grid(row=0, column=0, padx=5, pady=5)
        self.issue_book_id_entry = tk.Entry(self.issue_book_frame)
        self.issue_book_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.issue_user_id_label = tk.Label(self.issue_book_frame, text="User ID")
        self.issue_user_id_label.grid(row=1, column=0, padx=5, pady=5)
        self.issue_user_id_entry = tk.Entry(self.issue_book_frame)
        self.issue_user_id_entry.grid(row=1, column=1, padx=5, pady=5)

        self.issue_book_button = tk.Button(self.issue_book_frame, text="Issue Book", command=self.issue_book)
        self.issue_book_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Return Book
        self.return_book_frame = tk.LabelFrame(self.root, text="Return Book")
        self.return_book_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.return_book_id_label = tk.Label(self.return_book_frame, text="Book ID")
        self.return_book_id_label.grid(row=0, column=0, padx=5, pady=5)
        self.return_book_id_entry = tk.Entry(self.return_book_frame)
        self.return_book_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.return_user_id_label = tk.Label(self.return_book_frame, text="User ID")
        self.return_user_id_label.grid(row=1, column=0, padx=5, pady=5)
        self.return_user_id_entry = tk.Entry(self.return_book_frame)
        self.return_user_id_entry.grid(row=1, column=1, padx=5, pady=5)

        self.return_book_button = tk.Button(self.return_book_frame, text="Return Book", command=self.return_book)
        self.return_book_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def search_book(self):
        title = self.search_book_entry.get()
        if title:
            results = search_book(title)
            self.search_results_text.delete(1.0, tk.END)
            if results:
                for book in results:
                    self.search_results_text.insert(tk.END, f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Available: {'Yes' if book[3] else 'No'}\n")
            else:
                self.search_results_text.insert(tk.END, "No books found.")
        else:
            messagebox.showerror("Error", "Please enter a book title.")
    
    def add_book(self):
        title = self.book_title_entry.get()
        author = self.book_author_entry.get()
        if title and author:
            add_book(title, author)
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showerror("Error", "Please enter both title and author.")

    def add_user(self):
        name = self.user_name_entry.get()
        if name:
            add_user(name)
            messagebox.showinfo("Success", "User added successfully!")
        else:
            messagebox.showerror("Error", "Please enter a name.")

    def issue_book(self):
        book_id = self.issue_book_id_entry.get()
        user_id = self.issue_user_id_entry.get()
        if book_id and user_id:
            issue_book(book_id, user_id)
            messagebox.showinfo("Success", "Book issued successfully!")
        else:
            messagebox.showerror("Error", "Please enter both book ID and user ID.")

    def return_book(self):
        book_id = self.return_book_id_entry.get()
        user_id = self.return_user_id_entry.get()
        if book_id and user_id:
            return_book(book_id, user_id)
            messagebox.showinfo("Success", "Book returned successfully!")
        else:
            messagebox.showerror("Error", "Please enter both book ID and user ID.")

    
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()