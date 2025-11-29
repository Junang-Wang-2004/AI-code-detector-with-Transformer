v1 = int(input())
v2 = in_val // 100
v3 = in_val % 100 // 10
v4 = in_val % 10
if v2 == v3 and v2 == v4:
    print(in_val)
else:
    v2 = v2 + 1
    print('{}{}{}'.format(v2, v2, v2))
