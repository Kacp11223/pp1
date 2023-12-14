def f(binary_number):
    ones = binary_number.count('1')
    zeros = binary_number.count('0')
    return True if zeros + ones == len(binary_number) else False

print(f("100101010101"))