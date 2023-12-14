from math import pi

def shouldCut(circumference):
    return True if circumference/pi >= 50 else False
print(shouldCut(int(input())))