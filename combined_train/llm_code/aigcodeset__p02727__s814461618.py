import sys
import heapq

def f1(a1: int, a2: int, a3: int, a4: int, a5: int, a6: 'List[int]', a7: 'List[int]', a8: 'List[int]'):
    a6 = sorted(a6, reverse=True)
    a7 = sorted(a7, reverse=True)
    a8 = sorted(a8, reverse=True)
    v4 = 0
    for v5 in range(a1):
        if a6 and (not a8 or a6[0] > a8[0]):
            v4 += a6[0]
            del a6[0]
        elif a8:
            v4 += a8[0]
            del a8[0]
    for v5 in range(a2):
        if a7 and (not a8 or a7[0] > a8[0]):
            v4 += a7[0]
            del a7[0]
        elif a8:
            v4 += a8[0]
            del a8[0]
    print(v4)
    return

def f2(a1: int, a2: int, a3: int, a4: int, a5: int, a6: 'List[int]', a7: 'List[int]', a8: 'List[int]'):
    a6 = [-1 * i for v2 in a6]
    a7 = [-1 * v2 for v2 in a7]
    a8 = [-1 * v2 for v2 in a8]
    heapq.heapify(a6)
    heapq.heapify(a7)
    heapq.heapify(a8)
    v5 = 0
    for v2 in range(a1):
        if a6 and (not a8 or a6[0] < a8[0]):
            v6 = heapq.heappop(a6) * -1
            v5 += v6
        elif a8:
            v6 = heapq.heappop(a8) * -1
            v5 += v6
    for v2 in range(a2):
        if a7 and (not a8 or a7[0] < a8[0]):
            v6 = heapq.heappop(a7) * -1
            v5 += v6
        elif a8:
            v6 = heapq.heappop(a8) * -1
            v5 += v6
    print(v5)
    return

def f3():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = int(next(v1))
    v4 = int(next(v1))
    v5 = int(next(v1))
    v6 = int(next(v1))
    v7 = [int(next(v1)) for v8 in range(v4)]
    v9 = [int(next(v1)) for v8 in range(v5)]
    v10 = [int(next(v1)) for v8 in range(v6)]
    f1(v2, v3, v4, v5, v6, v7, v9, v10)
if __name__ == '__main__':
    f3()
