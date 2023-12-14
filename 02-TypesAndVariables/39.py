price = 24.72
discount = 0.15
newPrice = price*(1-discount)
format_newPrice = "{0:.2f}".format(newPrice)
reduction = price-newPrice
fromat_reduction = "{0:.2f}".format(reduction)
print(format_newPrice)
print(fromat_reduction)