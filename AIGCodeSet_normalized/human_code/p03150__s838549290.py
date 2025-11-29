import re

def f1():
    v1 = input()
    v2 = 'keyence'
    v3 = any((re.fullmatch(v2[:i] + '.*' + v2[i:], v1) for v4 in range(len(v2) + 1)))
    if v3:
        v3 = 'YES'
    else:
        v3 = 'NO'
    return str(v3)
if __name__ == '__main__':
    print(f1())
