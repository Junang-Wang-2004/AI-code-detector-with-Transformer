v1 = int(input())
v2 = float('inf')
print(0)
v3 = input()
if v3 == 'Male':
    v4 = 1
elif v3 == 'Female':
    v4 = 0
else:
    v2 = 0
if v2 == 0:
    exit(0)
v5 = [0, v1 - 1]
for v6 in range(19):
    v7 = (v5[1] - v5[0]) // 2
    print(v5[0] + v7)
    v3 = input()
    if v3 == 'Male':
        v8 = 1
    elif v3 == 'Female':
        v8 = 0
    else:
        exit(0)
    if v8 + v7 % 2 != v4:
        v5[1] = v5[0] + v7 - 1
    else:
        v5[0] = v5[0] + v7 + 1
        v4 = v8
    if v5[0] == v5[1]:
        print(v5[0])
        exit(0)
