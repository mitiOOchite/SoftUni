def check_employee_happiness():
    happiness_list = list(
        map(int, input().split()))  # create a list, map to integer everything input that is a result of the split
    happiness_factor = int(input())

    improved_happiness = [happiness * happiness_factor for happiness in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(happiness >= average_happiness for happiness in improved_happiness)
    total_count = len(improved_happiness)
    message = 'happy' if happy_count >= total_count / 2 else 'not happy'
    result = f'Score: {happy_count}/{total_count}. Employees are {message}!'
    return result


print(check_employee_happiness())
