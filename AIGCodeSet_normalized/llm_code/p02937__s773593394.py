import sys
v1 = input()
v2 = input()
v3 = 0
v4 = 0
while v3 < len(v2):
    if v4 == len(v1):
        v4 = 0
        v3 += 1
    if v2[v3] == v1[v4]:
        v3 += 1
    v4 += 1
if v3 == len(v2):
    print(v4 // len(v1) + 1)
else:
    print(-1)
