from math import floor
W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720
tournament_count = int(input())
starting_points = int(input())
gained_points = 0
total_wins = 0
for _ in range(tournament_count):
    tournament_result = input() # W F SF
    if tournament_result == "W":
        gained_points+=W_POINTS
        total_wins += 1
    elif tournament_result == "F":
        gained_points += F_POINTS
    elif tournament_result == "SF":
        gained_points += SF_POINTS
average_points = floor(gained_points/tournament_count)
w_percents = total_wins/tournament_count *100
total_points = starting_points + gained_points
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"Wins percent: {w_percents:.2f}%")