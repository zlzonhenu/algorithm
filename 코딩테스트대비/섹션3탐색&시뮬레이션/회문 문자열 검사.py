n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

for word in words:
    cnt = 0
    word = word.lower()
    rev_word = word[::-1]
    for i in range(len(word)//2):
        if word[i] == rev_word[i]:
            cnt+=1
    if cnt == len(word)//2 + 1:
        print("Yes")
    else:
        print("No")

#또 다른 풀이
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d No" % (i+1))
            break
    else:
        print("#%d Yes" % (i+1))

#또 다른 풀이
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s==s[::-1]:
        print("#%d Yes" % (i+1))
    else:
        print("#%d No" % (i+1))

