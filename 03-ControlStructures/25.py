from functools import partial
STOP = 'x'
input_with_prompt = partial(input, 'enter: ')
cart = [*iter(input_with_prompt, STOP), STOP][:-1]

cart = list(map(int, cart))
print(cart)
price = 0
for i in range(len(cart)):
    if i < 2:
        price += cart[i]
    else:
        price += cart[i]*0.75
print(price)
