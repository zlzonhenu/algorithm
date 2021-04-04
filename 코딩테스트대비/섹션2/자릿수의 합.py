#입력
N = int(input())
n = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    for s in x:
        sum += int(s)
    return sum

if __name__ == "__main__":
    max = 0
    for x in enumerate(n):
        str_x = str(x)
        tmp = digit_sum(str_x)
        if tmp > max:
            max = tmp
            res = x

    print(res)

#또다른 풀이
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)



