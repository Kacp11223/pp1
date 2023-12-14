def f(number, even):
    sum = 0
    while number > 0:
        if even:
            if (number%10)%2==0:
                sum += number%10
            number //= 10
        else:
            if (number%10)%2!=0:
                sum += number%10
            number //= 10
    return sum

print(f(13115,True))



