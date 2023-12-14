currentPrice = 120.00 #float(input("enter current price "))
previousPrice = 200.00#float(input("enter previous price "))
reduction = (1-(currentPrice/previousPrice))*100
if currentPrice <= previousPrice*0.9:
    print(f"Buy the product \nproduct price reduced by {reduction:.0f}%")