v1 = input()
v2 = [0, 0]
if 'N' in v1 and 'S' in v1 or ('N' not in v1 and 'S' not in v1):
    v2[0] = 1
if 'W' in v1 and 'E' in v1 or ('W' not in v1 and 'E' not in v1):
    v2[1] = 1
if sum(v2) == 2:
    print('Yes')
else:
    print('No')
