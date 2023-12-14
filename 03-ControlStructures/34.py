impmort numpy
cash = 40
denomyms = [25,20,10,5]
counts = []
def productMax(list):
    max = []
    for i in range(len(list)-1):
        if list[i] < len[i+1]:
            max = len[i+1]
def chChange(cash,denomyms,counts):
    if cash == 0:
        #finale = [[x[1], x[0]] for x in counts]
        return [(f"{x[1]} pln - {x[0]}") for x in counts]
    else:
        if counts == False:
            counts = min([[(cash//x),x] for x in denomyms if cash//x != 0])
        else:
            counts.append(min([[(cash//x),x] for x in denomyms if cash//x != 0]))
        cash %= counts[-1][-1]
        return chChange(cash,denomyms,counts)

[print(x) for x in chChange(cash,denomyms,counts)]