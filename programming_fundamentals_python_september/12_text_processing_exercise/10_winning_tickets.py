def check_ticket(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]  # slicing to get first 10 symbols of the ticket
    right_part = ticket[10:]  # slicing to get last 10 symbols of the ticket
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetition = match_symbol * uninterrupted_match_length
            # check if we have a winning ticket
            if winning_symbol_repetition in right_part and winning_symbol_repetition in left_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'

tickets = [ticket.strip() for ticket in input().split(', ')]
# strip removes whitespace intervals in the specified object

for current_ticket in tickets:
    print(check_ticket(current_ticket))
