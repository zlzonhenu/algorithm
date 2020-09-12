m = int(input())

count = 0
yen = [500, 100, 50, 10, 5, 1]
money = 1000-m
result = 0
for i in yen:
    if money >= i:
        count = money // i
        money -= count * i
        result += count
print(result)