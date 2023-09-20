# Входът е поредица от цели числа и текст:
# На първия ред до получаване на командата "Finish" - име на филма – текст
# На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# Типа на закупения билет - текст ("student", "standard", "kid")

command = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets =0
while command != "Finish":
    current_movie = command
    total_seats = int(input())
    available_seats = total_seats
    while available_seats > 0:
        current_ticket_type = input()  # End or [one of these "student", "standard", "kid"]
        if current_ticket_type == "End":
            break
        available_seats -= 1
        if current_ticket_type == "student":
            student_tickets += 1
        elif current_ticket_type == "standard":
            standard_tickets += 1
        elif current_ticket_type == "kid":
            kid_tickets += 1
    percent_full = (total_seats - available_seats) / total_seats * 100
    print(f"{current_movie} - {percent_full:.2f}% full.")
    command = input()
total_tickets = student_tickets+standard_tickets+kid_tickets
student_percent = student_tickets/total_tickets*100
standard_percent = standard_tickets/total_tickets*100
kid_percent = kid_tickets/total_tickets*100
print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")