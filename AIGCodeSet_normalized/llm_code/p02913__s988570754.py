v1 = int(input())
v2 = input()
for v3 in range(v1 // 2, 0, -1):
    for v4 in range(v1 - v3):
        if v2[v4:v4 + v3] in v2[v4 + v3:]:
            print(v3)
            exit()
print(0)
