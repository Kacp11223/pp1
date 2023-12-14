EAN_13 = "5901230094931"
if len(EAN_13) == 13:
    print("Article number is correct")
    if EAN_13[0:3] == "590":
        print("Article manufactured in Poland")
