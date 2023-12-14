dogAge = int(input("Enter the dog's age in human years: "))
if dogAge < 3:
    print("The dog's age in dog’s years is ",int(dogAge*10.5))
else:
    print("The dog's age in dog’s years is ",int((dogAge-2)*4)+21)