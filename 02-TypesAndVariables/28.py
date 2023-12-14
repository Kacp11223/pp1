height = int(input())
weight = int(input())

bmi = (weight/(height**2))*10000
if bmi >= 18.5 and bmi <= 24.9:
    print(f"good health {bmi}")
else:
    print(f"bad health {bmi}")