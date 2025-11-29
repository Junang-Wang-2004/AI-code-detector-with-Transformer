import collections

class C1(object):

    def countPartitions(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (collections.deque(), collections.deque())
        v4 = [0] * (len(a1) + 1)
        v4[0] = 1
        v5 = v6 = 0
        for v7 in range(len(a1)):
            v6 = (v6 + v4[v7]) % v1
            while v2 and a1[v2[-1]] <= a1[v7]:
                v2.pop()
            v2.append(v7)
            while v3 and a1[v3[-1]] >= a1[v7]:
                v3.pop()
            v3.append(v7)
            while a1[v2[0]] - a1[v3[0]] > a2:
                if v3[0] == v5:
                    v3.popleft()
                if v2[0] == v5:
                    v2.popleft()
                v6 = (v6 - v4[v5]) % v1
                v5 += 1
            v4[v7 + 1] = v6
        return v4[-1]
