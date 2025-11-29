def f1():
    v1, v2, v3 = map(int, input().split())
    return (v1, v2, v3)

def f2(a1, a2, a3):
    if a1 <= a2 * a3:
        return 'Yes'
    else:
        return 'No'
if __name__ == '__main__':
    v1, v2, v3 = f1()
    v4 = f2(v1, v2, v3)
    print(v4)
