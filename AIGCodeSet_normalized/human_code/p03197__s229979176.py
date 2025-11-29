v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
print('second' if all((v2[i] % 2 == 0 for v4 in range(v1))) else 'first')
