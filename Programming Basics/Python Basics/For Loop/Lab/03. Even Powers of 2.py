n = int(input())

for power in range(0, n + 1):
    if power % 2 == 0:
        print(pow(2, power))
