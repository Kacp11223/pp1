clothes = {"jacket":40, "underwear":70, "shoes":20}
rinse = True
spin = False
washTime = sum(list(clothes.values()))
if rinse:
    washTime += 15
if spin:
    washTime += 9
print(washTime)