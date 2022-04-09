#this exc is about adiction some values and has been
#chagend and improving and some fun, i think

price = float(input('what is the price of the product: '))

if price > 1000:
    priceOff = price - (price * 23 / 100)
elif price > 2000:
    priceOff = price - (price * 10 / 100)
elif price > 3000:
    priceOff = price - (price * 75 / 100)
else:
    priceOff = price - (price * 5 / 100)

print(f'The product was cost {price} and cost: {priceOff:.2f}')
