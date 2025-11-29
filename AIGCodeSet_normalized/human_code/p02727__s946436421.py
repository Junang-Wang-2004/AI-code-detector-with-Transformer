def f1():
    v1, v2, v3, v4, v5 = map(int, input().split())
    v6 = list(map(int, input().split()))
    v7 = list(map(int, input().split()))
    v8 = list(map(int, input().split()))
    v6.sort(reverse=True)
    v7.sort(reverse=True)
    v9 = v8 + v6[:v1] + v7[:v2]
    v9.sort(reverse=True)
    print(sum(v9[:v1 + v2]))
if __name__ == '__main__':
    f1()
