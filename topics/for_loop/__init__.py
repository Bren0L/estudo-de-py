"""

for name in ['breno', 'bruno', 'bred']:
    print(name)

for number in range(10):
    print(number)

for number in range(5, 10):
    print(number)

for number in range(5, 10, 2):
    print(number)

prices = [10, 20, 30]

print(sum(prices))

total = 0

for p in prices:
    total += p

print(total)"""

xs = [5, 2, 5, 2, 2]

for n in xs:
    s = ''
    for r in range(n):
        s += 'X'
    print(s)