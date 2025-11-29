v1 = int(input())
v2 = 0
v3 = 0
v4 = 0
v5 = 0
for v6 in range(v1):
    v7 = input()
    if v7 == 'AC':
        v2 = v2 + 1
    elif v7 == 'WA':
        v3 = v3 + 1
    elif v7 == 'TLE':
        v4 = v4 + 1
    elif v7 == 'RE':
        v5 = v5 + 1
print('AC x ', v2)
print('WA x ', v3)
print('TLE x ', v4)
print('RE x ', v5)
