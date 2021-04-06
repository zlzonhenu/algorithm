s = input()

n = 0
for i in s:
    if i.isdigit():
        n = n*10+int(i)
n = int(n)
cnt = 0
for j in range(1, n+1):
    if n % j == 0:
        cnt += 1
print(n)
print(cnt)