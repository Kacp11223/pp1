from functools import partial
STOP = "0"
input_with_prompt = partial(input, "enter: ")
numbers = [*iter(input_with_prompt,STOP), STOP][:-1]
prod = 0
for x in numbers:
    prod += int(x)
mean = prod//len(numbers)
print(mean)