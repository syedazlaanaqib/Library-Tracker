# library.py
# A simple command-line library tracker.

books = {}  # title -> {"author": str, "available": bool}


def show_menu():
    print("\n== Library Tracker ===")
    print("2. List books")
    print("0. Exit")

def list_books():
    if not books:
        print("No books in the library.")
        return
    for title, info in books.items():
        status = "Available" if info["available"] else "Borrowed"
        print(f"{title} by {info['author']} - {status}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "2":
            list_books()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()