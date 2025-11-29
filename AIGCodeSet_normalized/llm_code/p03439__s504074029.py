v1 = int(input())
print(0, flush=True)
v2 = input()
v3 = 0
v4 = v1 - 1
while True:
    print(v3 + (v4 - v3) // 2, flush=True)
    v5 = input()
    if v2 != v5:
        if v4 - v3 == 2:
            print(v3 + 2, flush=True)
        v4 = v3 + (v4 - v3) // 2
    else:
        if v4 - v3 == 2:
            print(v3, flush=True)
        v3 = v3 + (v4 - v3) // 2
