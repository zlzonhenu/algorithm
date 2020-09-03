n, m = map(int, input().split())

result = []
for i in range(n):
    x = list(map(int, input().split()))
    result.append(min(x))
print(max(result))

