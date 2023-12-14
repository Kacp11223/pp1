arr = [[-38, 19],[5,40],[-7,11],[29,16]]
mins = [(min(x),x.index(min(x)),arr.index(x)) for x in arr]
print(mins)
maxs = [(max(x),x.index(max(x)),arr.index(x)) for x in arr]
print(maxs)

mins = min(mins)
maxs = max(maxs)
print(mins)
print(maxs)