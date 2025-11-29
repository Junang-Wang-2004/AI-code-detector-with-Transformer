v1 = int(input())
v2 = []
for v3 in range(32):
    v4 = (-2) ** v3
    if v1 >= v4:
        v1 -= v4
        v2.append('1')
    else:
        v2.append('0')
while v2[-1] == '0' and len(v2) > 1:
    v2.pop()
print(''.join(v2[::-1]))
