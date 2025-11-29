v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
print('second' if all((v2[v3] % 2 == 0 for v3 in range(v1))) else 'first')
