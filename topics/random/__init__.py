import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))  # it will generate values between 10 and 20

# choosing a person randonly
team = ["Breno", "Bruno", "Bred", "Brenna", "Brenda"]

print(random.choice(team))


class Dice:
    def roll(self):
            n1 = random.randint(1, 6)
            n2 = random.randint(1, 6)
            return n1, n2


dice = Dice()
print(dice.roll())
