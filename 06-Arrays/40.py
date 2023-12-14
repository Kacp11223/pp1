import random
main = [f'|   {random.randint(1,999)}' for x in range(8)]
strain = "".join([str(x) for x in main])
[print("-",end='') for x in range(len(strain)+1)]
print()
print(strain,end="")
print('|')
[print("-",end='') for x in range(len(strain)+1)]

