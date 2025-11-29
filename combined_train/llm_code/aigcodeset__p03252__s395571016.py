import sys
v1 = input()
v2 = input()
v3 = {}
v4 = {}
for v5 in range(len(v2)):
    if v1[v5] != v2[v5]:
        if v1[v5] in v3:
            if v3[v1[v5]] != v2[v5]:
                print('No')
                sys.exit(0)
        if v2[v5] in v4:
            if v4[v2[v5]] != v1[v5]:
                print('No')
                sys.exit(0)
        if v1[v5] in v3 or v2[v5] in v4:
            print('No')
            sys.exit(0)
        v3[v1[v5]] = v2[v5]
        v4[v2[v5]] = v1[v5]
print('Yes')
