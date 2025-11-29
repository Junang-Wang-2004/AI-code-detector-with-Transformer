from collections import deque

class C1(object):

    def minMutation(self, a1, a2, a3):
        """
        """
        v1 = {}
        for v2 in a3:
            v1[v2] = False
        v3 = deque([(a1, 0)])
        while v3:
            v4, v5 = v3.popleft()
            if v4 == a2:
                return v5
            for v6 in range(len(v4)):
                for v7 in ['A', 'T', 'C', 'G']:
                    if v4[v6] == v7:
                        continue
                    v8 = v4[:v6] + v7 + v4[v6 + 1:]
                    if v8 in v1 and v1[v8] == False:
                        v3.append((v8, v5 + 1))
                        v1[v8] = True
        return -1
