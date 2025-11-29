v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sum(v2)
v4 = 0
while True:
    if v3 % 2 == 0:
        v3 /= 2
        v4 += 1
    else:
        break
print(v4)
