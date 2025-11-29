import sys

def f1():
    v1 = sys.stdin.readline().strip().split('/')
    v2, v3, v4 = [int(i) for v5 in v1]
    if v2 < 2019:
        print('Heisei')
    elif v2 == 2019:
        if v3 < 4:
            print('Heisei')
        elif v3 == 4:
            if v4 <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')
if __name__ == '__main__':
    f1()
