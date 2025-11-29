v1 = int(input())
print(0)
v2 = input()
v3 = 0
v4 = v1 - 1
while True:
    print(v2)
    print(v3 + (v4 - v3) // 2)
    v5 = input()
    if v2 != v5:
        if (v3 - v4) // 2 <= 1:
            print(v4)
        v4 = v3 + (v4 - v3) // 2
    else:
        if (v3 - v4) // 2 <= 1:
            print(v3)
        v3 = v3 + (v4 - v3) // 2
        v2 = v5
