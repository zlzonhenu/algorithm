n = int(input())
data = list(map(int, input().split()))

data.sort()
a = 0
b = 0
for i in data:
    a += i + b
    b += i
print(a)