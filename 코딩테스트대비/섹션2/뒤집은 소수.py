n = int(input())
a = list(map(int, input().split()))


def reverse(x):
    str_x = str(x)
    k = ""
    for s in reversed(str_x):
        if int(s) != 0:
            k += s
    return int(k)

def isPrime(x):
    b = 0
    for i in range(2, x):
        if x%i == 0:
            b = 1
    if b == 1:
        res = 1
    else:
        res = 0
    return res, x

for x in a:
    tmp = reverse(x)
    res, y = isPrime(tmp)
    if res == 0:
        print(y, end =" ")
