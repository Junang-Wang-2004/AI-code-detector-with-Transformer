v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
if sum(v2) % 2 == 0:
    print('second')
else:
    print('first')
