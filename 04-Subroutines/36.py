def f(s):
    count = 0
    for x in s:
        if x == '+':
            count += 1
            if count == 3:
                return True
        else:
            count -= 1
    return False
        
    

print(f("+-++-++-+---"))