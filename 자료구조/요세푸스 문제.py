N, K = map(int, input().split())
circle_list = [i+1 for i in range(N)]
popIndex = 0
answer = []
while len(circle_list) > 0:
    popIndex = (popIndex+(K-1)) % len(circle_list)
    popElement = circle_list.pop(popIndex)
    answer.append(str(popElement))

print("<%s>" % (", ".join(answer)))