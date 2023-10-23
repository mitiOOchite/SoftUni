days = int(input())
players = int(input())
totalEnergy = float(input())
personWater = float(input())
personFood = float(input())
totalWater = 0.0
totalWater = float(days * players * personWater)
totalFood = 0.0
totalFood = float(days * players * personFood)
waterDay = 0
foodDay = 0
for day in range(days):
    wastedEnergy = float(input())
    totalEnergy -= wastedEnergy
    if totalEnergy <= 0.0:
        break
    waterDay += 1
    if waterDay >= 2:
        totalWater -= totalWater * 0.3
        totalEnergy += totalEnergy * 0.05
        waterDay = 0
    foodDay += 1
    if foodDay >= 3:
        totalFood -= (totalFood / players)
        totalEnergy += totalEnergy * 0.1
        foodDay = 0

if totalEnergy >= 1:
    print(f"You are ready for the quest. You will be left with - {totalEnergy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {totalFood:.2f}"
          f" food and {totalWater:.2f} water.")