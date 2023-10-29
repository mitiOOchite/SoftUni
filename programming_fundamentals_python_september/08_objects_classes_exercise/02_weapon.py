class Weapon:
    def __init__(self,bullets:int):
        self.bullets = bullets
    def shoot(self):
        if self.bullets > 0:
            self.bullets -=1
            return "shooting..."
        return "no bullets left"

    def __repr__(self): #prints the value from the object as string represented
        return f'Remaining bullets: {self.bullets}'

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)