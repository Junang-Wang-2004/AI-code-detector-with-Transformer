import re
v1 = input()
v2 = 'keyence'
v3 = False
for v4 in range(0, len(v2)):
    v5 = v2[:v4 + 1]
    v6 = v2[-(len(v2) - v4 - 1):]
    v7 = v1.find(v5)
    v8 = v1.rfind(v6)
    if v7 < 0 or v8 < 0:
        continue
    elif v7 == 0:
        if v8 == len(v1) - len(v6):
            v3 = True
if v1.find(v2) >= 0 and v1.find(v2) == len(v1) - len(v2):
    v3 = True
if v1.find(v2) == 0:
    v3 = True
if v3:
    print('YES')
else:
    print('NO')
