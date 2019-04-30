
def budget(keyboards, drives, b):
    maxSum = 0
    for kb in keyboards:
        for dr in drives:
            price = kb + dr
            print(price, maxSum)
            if (price == b):
                return b
            if (price < b and price > maxSum):
                maxSum = price
    if (maxSum == 0):
        return -1

print(budget([3,1],[5,2,8],10))