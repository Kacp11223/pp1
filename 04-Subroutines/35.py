def f(n1,n2,operator):
    if operator == "+":
        return n1 + n2
    if operator == "-":
        return n1 - n2
    if operator == "*":
        return n1 * n2
    if operator == "%":
        return n1 % n2
    if operator == "**":
        return n1 ** n2
    
print(f(2,3,"-"))