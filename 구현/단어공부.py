Word = input().upper()
t = []
for i in set(Word):
    t.append(Word.count(i))
idx = [i for i,x in enumerate(t) if x==max(t)]
if len(idx) > 1:
    print("?")
else:
    print(list(set(Word))[t.index(max(t))])
