time = int(input())
if time > 1200:
    time-=1200
time = str(time)
if len(time) < 4:
    print(time[:1] + ":" + time[1:])
else:
    print(time[:2] + ":" + time[2:])