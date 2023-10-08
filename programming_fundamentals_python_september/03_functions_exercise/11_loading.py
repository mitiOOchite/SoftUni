def loading_bar(some_number:int) -> str:
    if some_number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    loaded_percent = some_number // 10
    percent_signs= '%'*loaded_percent
    dot_signs = '.'*(10-loaded_percent)
    return f'{some_number}% [{percent_signs}{dot_signs}]\nStill loading...'

number = int(input())
print(loading_bar(number))