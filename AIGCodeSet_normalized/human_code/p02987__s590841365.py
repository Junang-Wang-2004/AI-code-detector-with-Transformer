import collections
v1 = input()
v2 = collections.Counter(v1)
if v2.most_common()[0][1] == 2 and v2.most_common()[1][1] == 2:
    print('Yes')
else:
    print('No')
