v1 = int(input())
v2 = [v1]

def f1(a1):
    if a1 % 2 == 0:
        return a1 // 2
    else:
        return 3 * a1 + 1
v3 = 0
while True:
    if f1(v2[v3]) in v2:
        print(v3 + 2)
        break
    v2.append(f1(v2[v3]))
    v3 += 1
