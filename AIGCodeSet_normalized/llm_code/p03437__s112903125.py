import fractions as f
v1, v2 = map(int, input().split())
if v1 == 1:
    if v2 == 1:
        print(-1)
    else:
        print(1)
elif v2 == 1:
    print(2)
elif v1 % v2 == 0 or v2 % v1 == 0:
    print(-1)
else:
    v3 = v1 * v2 // f.gcd(v1, v2) - v1
    print(v3)
