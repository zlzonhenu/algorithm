a = list(map(str, input()))

b = []
sum = 0
for i in range(len(a)):
    if a[i] == '(':
        b.append(a[i])
    #레이저인지 확인하기 위해 전인덱스 확인
    elif a[i] == ')':
        if a[i-1] == '(':
            b.pop()
            # 스택에 남아있는 게 막대기 갯수
            sum += len(b)
        #레이저가 아닐때 막대 끝점이 생기면서 하나 추가
        else:
            b.pop()
            sum += 1
print(sum)