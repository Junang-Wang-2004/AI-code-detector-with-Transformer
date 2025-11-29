def f1(a1):
    v1, v2 = a1.split()
    if len(v1) == 1:
        return v1
    v3 = 0
    for v4 in str(v1):
        if v4 == '1':
            v3 += 1
            continue
        break
    return '1' if len(v2) < 4 and int(v2) <= v3 else v1[v3]
if __name__ == '__main__':
    print(f1('\n'.join([input(), input()])))
