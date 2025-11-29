v1, v2 = list(map(int, input().split()))
print((v2 * 1900 + (v1 - v2) * 100) * 2 ** v2)
