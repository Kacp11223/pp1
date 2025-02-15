Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

def hotel_list(l):
    return ' '.join([x["name"] for x in l])

def avg_price(l):
    return sum([x["price"] for x in l])/len(l)

print(hotel_list(Hotels_in_Krakow))
print(avg_price(Hotels_in_Krakow))