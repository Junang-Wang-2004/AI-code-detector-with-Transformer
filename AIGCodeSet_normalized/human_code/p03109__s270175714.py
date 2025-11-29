import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
v1 = input()
v2 = v1.split('/')
v3 = 'Heisei'
if int(v2[0]) > 2019:
    v3 = 'TBD'
elif v2[0] == '2019':
    if int(v2[1]) > 4:
        v3 = 'TBD'
print(v3)
