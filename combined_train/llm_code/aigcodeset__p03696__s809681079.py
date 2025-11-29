import re
if __name__ == '__main__':
    v1 = int(input())
    v2 = input()
    v3 = 0
    v2 = v2.replace('()', '1')
    v4 = v2.count('(')
    v5 = v2.count(')')
    if v4 == 0 and v5 == 0:
        v2 = v2.replace('1', '()')
        print(v2)
        exit(0)
    if v4 > v5:
        v3 = abs(v4 - v5)
        for v6 in range(v3):
            v2 = v2 + ')'
    if v5 > v4:
        v3 = abs(v4 - v5)
        for v6 in range(v3):
            v2 = '(' + v2
    if v5 == v4:
        for v6 in range(v5):
            v2 = v2 + ')'
        for v6 in range(v4):
            v2 = '(' + v2
    v2 = v2.replace('1', '()')
    print(v2)
