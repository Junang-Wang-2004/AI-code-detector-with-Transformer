if __name__ == '__main__':
    v1 = input()
    v2 = input()
    v3 = len(v2)
    for v4 in range(len(v1) - len(v2) + 1):
        v5 = 0
        for v6 in range(len(v2)):
            if v2[v6] != v1[v4 + v6]:
                v5 += 1
        v3 = min(v3, v5)
    print(v3)
