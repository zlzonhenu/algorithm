N = int(input())
stack = list()
cmd = list()
for i in range(N):
    cmd.append(input())
for command in cmd:
    if command.split()[0] == "push":
        stack.append(command.split()[1])
    elif command == "pop":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])