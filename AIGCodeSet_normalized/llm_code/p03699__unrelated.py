v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v4 = sum(v2)
v5 = v4
while v5 % 10 == 0:
    v5 -= 1
print(v5)
