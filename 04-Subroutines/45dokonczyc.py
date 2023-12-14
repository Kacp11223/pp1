def f(s):
    s = list(s)
    sum = 0
    for i in range(0,len(s),3):
        if s[i+1] == '+':
            sum += int(s[i])+int(s[i+2])
            s[i+2] = str(sum)
        else:
            sum += int(s[i])-int(s[i+2])
            s[i+2] = str(sum)
    return sum

print(f("2+3+2"))
