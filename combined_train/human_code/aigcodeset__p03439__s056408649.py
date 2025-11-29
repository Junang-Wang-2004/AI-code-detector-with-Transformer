v1 = int(input())
print(0, flush=True)
v2 = input()
if v2 == 'Vacant':
    exit()
v3 = v2
v4 = 0
print(v1 - 1, flush=True)
v2 = input()
if v2 == 'Vacant':
    exit()
v5 = v2
v6 = v1 - 1
while True:
    v7 = (v4 + v6) // 2
    print(v7, flush=True)
    v8 = input()
    if v8 == 'Vacant':
        exit()
    if v5 == v8 and (v6 - v7) % 2 == 1 or (v5 != v8 and (v6 - v7) % 2 == 0):
        v4 = v7
        v3 = v8
    else:
        v6 = v7
        v5 = v8
