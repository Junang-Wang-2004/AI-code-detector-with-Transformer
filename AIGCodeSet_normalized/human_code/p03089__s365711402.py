v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = []
while len(v2) > 0:
    for v3 in range(len(v2) - 1, -1, -1):
        if v2[v3] == v3 + 1:
            v4.append(v3 + 1)
            del v2[v3]
            break
    else:
        print(-1)
        exit()
print(*v4[::-1], sep='\n')
