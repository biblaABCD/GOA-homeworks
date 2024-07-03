item_quantity = int(input('amount of items you want: '))

if item_quantity > 0:
    price = int(input('Enter prices of items you want: '))

if item_quantity < 0:
    print(False)

if price < 0:
    print(False)

else:
    print(False)

print(item_quantity + price)

