if __name__ == '__main__':
    v1, v2 = list(map(int, input().split()))
    v3 = sorted([input() for v4 in range(v1)])
    print(''.join(v3))
