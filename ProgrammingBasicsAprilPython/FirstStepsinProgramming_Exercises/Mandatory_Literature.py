book_pages = int(input())
pages_per_hour = int(input())
book_days = int(input())
total_hours = book_pages // pages_per_hour#wholenumber division - takes only the first digit does not round
hours_per_day = total_hours/book_days
print(int(hours_per_day))