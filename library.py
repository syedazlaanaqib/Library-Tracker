# library.py
# A simple command-line library tracker.

books = {}  # title -> {"author": str, "available": bool}


def show_menu():
    print("\n== Library Tracker ===")
    print("2. List books")
    print("1. Add book")
    print("4. Return book")
    print("0. Exit")

def add_book():
    title = input("Title: ")
    if title in books:
        print(f'"{title}" is already in the library.')
        return
    author = input("Author: ")
    books[title] = {"author": author, "available": True}
    print(f'Added "{title}".')

def list_books():
    if not books:
        print("No books in the library.")
        return
    for title, info in books.items():
        status = "Available" if info["available"] else "Borrowed"
        print(f"{title} by {info['author']} - {status}")

def return_book():
    title = input("Title: ")
    if title not in books:
        print(f'No book titled "{title}".')
        return
    if books[title]["available"]:
        print(f'"{title}" is not borrowed.')
        return
    books[title]["available"] = True
    print(f'You returned "{title}".')


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "2":
            list_books()
        elif choice == "1":
            add_book()
        elif choice == "4":
            return_book()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()