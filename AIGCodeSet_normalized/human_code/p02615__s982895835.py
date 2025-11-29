import queue
import sys

def f1():
    return sys.stdin.readline().rstrip('\n')

def f2(a1, a2):
    a2.sort(key=lambda x: -x)
    v1 = queue.Queue()
    v1.put(a2[0])
    v2 = 0
    for v3 in a2[1:]:
        v2 += v1.get()
        v1.put(v3)
        v1.put(v3)
    return v2
v1 = int(f1())
v2 = [int(s) for v3 in f1().split()]
print(f2(v1, v2))
