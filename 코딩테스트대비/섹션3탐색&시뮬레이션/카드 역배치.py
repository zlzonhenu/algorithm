n = [x for x in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    size = b - a
    for i in range((size+1)//2):
        n[a+i], n[b-i] = n[b-i], n[a+i]

n.pop(0)
for y in n:
    print(n, end=" ")