v1 = int(input())
v2 = input()
v3 = int(input())
for v4 in range(v3):
    v5 = input().split()
    if v5[0] == '1':
        v6 = int(v5[1]) - 1
        v7 = v5[2]
        if v2[v6] != v7:
            v2 = v2[:v6] + v7 + v2[v6 + 1:]
    elif v5[0] == '2':
        v8 = int(v5[1]) - 1
        v9 = int(v5[2]) - 1
        v10 = v2[v8:v9 + 1]
        v11 = set(v10)
        print(len(v11))
