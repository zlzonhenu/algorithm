number = input().split("-")
sum = 0

for i in number[0].split("+"):
    sum += int(i)

for i in number[1:]:
    for j in i.split("+"):
        sum -= int(j)
print(sum)