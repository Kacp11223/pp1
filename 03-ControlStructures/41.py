PIN = "0805"
i = 0
for tries in range(3):
    if input() == PIN:
        print("correct PIN")
        break
    else:
        print("incorrect...")
        i += 1
if i == 3:
    print("Sorry, your payment card has been blocked.")
    
