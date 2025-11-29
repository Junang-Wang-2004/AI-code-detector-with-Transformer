v1 = int(input())
v2 = [v1]
while True:
    if v2[-1] % 2 == 0:
        v2.append(v2[-1] // 2)
    else:
        v2.append(v2[-1] * 3 + 1)
    for v3 in range(0, len(v2) - 1):
        if v2[-1] == v2[v3]:
            break
    else:
        continue
    break
print(len(v2))
