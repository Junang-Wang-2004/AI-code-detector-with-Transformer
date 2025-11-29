v1, v2 = list(map(int, input().split()))
print((1900 * v2 + 100 * (v1 - v2)) * 2 ** v2)
