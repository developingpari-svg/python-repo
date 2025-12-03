from functools import reduce   # <-- you forgot this import

l = [12, 12, 12, 12, 21, 21, 32]

sum_fn = lambda x, y: x + y

# map → square list
square = lambda x: x**2
squareList = list(map(square, l))
print(squareList)

# filter → only even numbers
onlyeven = lambda x: x % 2 == 0
onlyevenList = list(filter(onlyeven, l))
print(onlyevenList)

# reduce → sum of all numbers
totalsum = reduce(sum_fn, l)
print(totalsum)
