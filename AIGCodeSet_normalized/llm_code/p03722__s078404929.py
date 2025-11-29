def f1(a1: int, a2: list, a3: int) -> list:
    v1 = [float('inf')] * a1
    v1[a3] = 0
    for v2 in range(a1 - 1):
        for v3, v4, v5 in a2:
            v1[v4] = min(v1[v4], v1[v3] + v5)
    for v3, v4, v5 in a2:
        if v1[v3] + v5 < v1[v4]:
            v1[v4] = float('-inf')
    return v1

def f2(a1: int, a2: int, a3: list) -> int:
    v1 = f1(a1, [(u - 1, v - 1, -c) for v2, v3, v4 in a3], 0)
    return -v1[a1 - 1] if v1[a1 - 1] != float('-inf') else float('inf')
if __name__ == '__main__':
    v1 = 0
    v2, v1 = map(int, input().split())
    v3 = [tuple(map(int, input().split())) for v4 in range(v1)]
    v5 = f2(v2, v1, v3)
    print(v5)
