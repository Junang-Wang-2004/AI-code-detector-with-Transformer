v1 = input()
v2 = set(v1)
if len(v2) == 2:
    v3 = [v1.count(char) for v4 in v2]
    if v3 == [2, 2]:
        print('Yes')
    else:
        print('No')
else:
    print('No')
