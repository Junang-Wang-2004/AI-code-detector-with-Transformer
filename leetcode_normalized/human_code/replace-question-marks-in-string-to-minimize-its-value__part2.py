import heapq

class C1(object):

    def minimizeStringValue(self, a1):
        """
        """

        def counting_sort(a1):
            for v1 in range(len(a1)):
                for v2 in range(a1[v1]):
                    yield v1
        v1 = [0] * 26
        for v2 in a1:
            if v2 == '?':
                continue
            v1[ord(v2) - ord('a')] += 1
        v3 = [(v2, i) for v4, v2 in enumerate(v1)]
        heapq.heapify(v3)
        v5 = [0] * 26
        for v6 in range(a1.count('?')):
            v7, v4 = heapq.heappop(v3)
            heapq.heappush(v3, (v7 + 1, v4))
            v5[v4] += 1
        v8 = counting_sort(v5)
        v9 = list(a1)
        for v4 in range(len(v9)):
            if v9[v4] != '?':
                continue
            v9[v4] = chr(ord('a') + next(v8))
        return ''.join(v9)
