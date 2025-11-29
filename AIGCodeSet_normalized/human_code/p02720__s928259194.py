v1 = int(input())
v2 = 0
import queue
v3 = queue.Queue()
for v4 in range(1, 10):
    v3.put(v4)
while True:
    v5 = v3.get()
    v2 += 1
    if v2 == v1:
        break
    elif v5 % 10 != 9 and v5 % 10 != 0:
        v3.put(10 * v5 + v5 % 10 - 1)
        v3.put(10 * v5 + v5 % 10)
        v3.put(10 * v5 + v5 % 10 + 1)
    elif v5 % 10 == 9:
        v3.put(10 * v5 + v5 % 10 - 1)
        v3.put(10 * v5 + v5 % 10)
    else:
        v3.put(10 * v5 + v5 % 10)
        v3.put(10 * v5 + v5 % 10 + 1)
print(v5)
