import collections

class C1:

    def countPartitions(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [0] * (v2 + 1)
        v3[0] = 1
        v4 = [0] * (v2 + 2)
        v4[1] = 1
        v5 = 0
        v6 = collections.deque()
        v7 = collections.deque()
        for v8 in range(v2):
            while v6 and a1[v6[-1]] <= a1[v8]:
                v6.pop()
            v6.append(v8)
            while v7 and a1[v7[-1]] >= a1[v8]:
                v7.pop()
            v7.append(v8)
            while v5 <= v8 and a1[v6[0]] - a1[v7[0]] > a2:
                if v6 and v6[0] == v5:
                    v6.popleft()
                if v7 and v7[0] == v5:
                    v7.popleft()
                v5 += 1
            v3[v8 + 1] = (v4[v8 + 1] - v4[v5] + v1) % v1
            v4[v8 + 2] = (v4[v8 + 1] + v3[v8 + 1]) % v1
        return v3[v2]
