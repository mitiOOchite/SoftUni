book_name = input()
searched_book = input()
book_count = 0
while searched_book != "No More Books":
    current_book = searched_book
    if current_book == book_name:
        book_count += 1
        break
    searched_book = input()
    book_count += 1
if current_book != "No More Books":
    print(f"{book_name}, you checked {book_count}")
else:
    print("The book you search is not here")
    print(f"You checked {book_count} books")