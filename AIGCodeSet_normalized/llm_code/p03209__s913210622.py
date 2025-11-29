v1 = input().split()
v2 = int(v1[0])
v3 = int(v1[1])
v4 = 'P'
for v5 in range(v2):
    v4 = 'B' + v4 + 'P' + v4 + 'B'
    if len(v4) >= v3:
        break
v4 = v4[-v3:]
print(v4.count('P'))
