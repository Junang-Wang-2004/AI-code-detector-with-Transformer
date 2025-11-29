v1 = input().split()
v2 = sorted(v1)
if int(v2[2]) == int(v2[0]) + int(v2[1]) or int(v2[0]) == int(v2[1]) + int(v2[2]) or int(v2[0]) == int(v2[1]) == int(v2[2]):
    print('Yes')
else:
    print('No')
