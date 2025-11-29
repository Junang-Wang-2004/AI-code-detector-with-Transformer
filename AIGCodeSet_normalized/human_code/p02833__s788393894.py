v1 = int(input())
if v1 % 2:
    print(0)
    exit()
v2 = 0
v3 = 10
while v3 <= 10 ** 18:
    v2 += v1 // v3
    v3 *= 5
print(v2)
