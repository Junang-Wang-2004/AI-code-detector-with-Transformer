v1 = int(input())
v2 = 0
v3 = 0
for v4 in range(v1):
    v5 = int(input())
    v2 = max(v5, v2)
    v3 += v5
if v2 == 1:
    print('first')
elif (v3 - 2) % 2 == 1:
    print('first')
else:
    print('second')
