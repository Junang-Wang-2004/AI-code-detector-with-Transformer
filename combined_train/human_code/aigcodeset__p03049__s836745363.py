v1 = int(input())
v2 = 0
v3 = 0
v4 = 0
v5 = 0
for v6 in range(0, v1):
    v7 = input()
    v2 = v2 + v7.count('AB')
    if v7[0] == 'B' and v7[-1] == 'A':
        v5 = v5 + 1
    elif v7[0] == 'B':
        v4 = v4 + 1
    elif v7[-1] == 'A':
        v3 = v3 + 1
v2 = v2 + v5
if v3 == 0 and v4 == 0 and (v5 != 0):
    v2 = v2 - 1
elif v4 >= v3:
    v2 = v2 + v3
else:
    v2 = v2 + v4
print(v2)
