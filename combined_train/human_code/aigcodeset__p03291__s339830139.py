v1 = 10 ** 9 + 7
v2 = input()

def f1(a1, a2):
    """各位置について，それより左の文字列に含まれる文字 c の総数.
       左に'?'が含まれるときは，それらに文字を入れて得られるすべての
       文字列に渡って，文字 c の個数を合計する. """
    v1 = [0 for a2 in a1]
    for v2 in range(1, len(a1)):
        v1[v2] = v1[v2 - 1] + (1 if a1[v2 - 1] == a2 else 0)
    v3 = 0
    v4 = 1
    for v2 in range(len(v1)):
        if v3 > 0:
            v1[v2] *= v4
            v1[v2] += pow3q1 * v3
            v1[v2] %= v1
        if a1[v2] == '?':
            v3 += 1
            v5 = v4
            v4 = v4 * 3 % v1
    return v1

def f2(a1, a2):
    v1 = [0 for a2 in a1]
    for v2 in range(len(a1) - 1, 0, -1):
        v1[v2 - 1] = v1[v2] + (1 if a1[v2] == a2 else 0)
    v3 = 0
    v4 = 1
    for v2 in range(len(v1) - 1, -1, -1):
        if v3 > 0:
            v1[v2] *= v4
            v1[v2] += pow3q1 * v3
            v1[v2] %= v1
        if a1[v2] == '?':
            v3 += 1
            v5 = v4
            v4 = v4 * 3 % v1
    return v1
v3 = f1(v2, 'A')
v4 = f2(v2, 'C')
v5 = 0
for v6 in range(0, len(v2)):
    if v2[v6] in 'B?':
        v5 += v3[v6] * v4[v6]
v5 = int(v5) % v1
print(v5)
