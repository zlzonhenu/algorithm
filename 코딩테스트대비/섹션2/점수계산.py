n = int(input())
a = list(map(int, input().split()))

cnt = 0
sum = 0
for i in range(n):
    if a[i] == 1:
        cnt += 1
    else:
        cnt = 0
    sum += cnt
print(sum)