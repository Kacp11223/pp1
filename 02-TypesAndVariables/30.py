import random
roll = random.randrange(1,7)
print("Dice rolled ",roll)
if roll == 1 or roll == 6:
    print("special number ", True)
else:
    print("special number ", False)