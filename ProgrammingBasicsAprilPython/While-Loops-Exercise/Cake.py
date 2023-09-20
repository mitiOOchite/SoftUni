cake_width = int(input())
cake_length = int(input())
cake_pieces_total = cake_length * cake_width
cake_piece_left = cake_pieces_total

while True:
    command = input() #STOP or integer as string
    if command == "STOP":
        break
    current_pieces = int(command)
    cake_piece_left -= current_pieces
    if cake_piece_left <= 0:
        break
if cake_piece_left > 0:
    print(f"{cake_piece_left} pieces are left")
else:
    print(f"No more cake left! You need {abs(cake_piece_left)} pieces more")