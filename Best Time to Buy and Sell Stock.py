# prices = [7, 1, 5, 3, 6, 4]
prices = [7,6,4,3,1]
if not prices:
    print(0)
max_price = 0
min_price = prices[0]
for price in prices:
    min_price = min(min_price, price)
    diff = price - min_price
    max_price = max(max_price, diff)
print(max_price)