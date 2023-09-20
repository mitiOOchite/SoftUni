# •	Всички до 16 (вкл.) години се считат за деца и ще получат играчка age <= 16 = kid = toy
# •	Всички над 16 години се считат за възрастни и ще получат коледен пуловер age > 16 = adult = sweatshirt
# •	Цената на всяка играчка е 5 лв., а цената на един пуловер е 15 лв.
# Напишете програма, която пресмята колко души от семейството на Иван са до 16 (вкл.)
# колко са над тази възраст, също и колко пари ще струват подаръците на децата и възрастните.
# •	"Number of adults: {брой хора над 16 години}"
# •	"Number of kids: {брой хора до 16 (вкл.) години}"
# •	"Money for toys: {сумата за всички играчки}"
# •	"Money for sweaters: {сума за всички пуловери}"

END_COMMAND = "Christmas"
age = 0
toy_price = 5
sweatshirt_price = 15
kid_count = 0
adult_count = 0
total_toy_price = 0
total_adult_price = 0
command = input()
while True:
    if command == END_COMMAND:
        break
    elif int(command) <= 16:
        kid_count+=1
        command = input()
    elif int(command) > 16:
        adult_count+=1
        command = input()
total_adult_price = adult_count*sweatshirt_price
total_toy_price = kid_count*toy_price
print(f"Number of adults: {adult_count}")
print(f"Number of kids: {kid_count}")
print(f"Money for toys: {total_toy_price}")
print(f"Money for sweaters: {total_adult_price}")
