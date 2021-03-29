#입력
cases = int(input())

input_lists = []
number_lists = []
for _ in range(cases):
    input_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    input_lists.append(input_list)
    number_lists.append(number_list)


for i in range(cases):
    K = sorted(number_lists[i][input_lists[i][1]-1:input_lists[i][2]-1])
    j = K[input_lists[i][3]-1]
    print("#%d: %d" % (i+1, j))