class C1(object):

    def topKFrequent(self, a1, a2):
        """
        """

        class MinHeapObj(object):

            def __init__(self, a1):
                self.val = a1

            def __lt__(self, a1):
                return self.val[1] > a1.val[1] if self.val[0] == a1.val[0] else self.val < a1.val

            def __eq__(self, a1):
                return self.val == a1.val

            def __str__(self):
                return str(self.val)
        v1 = collections.Counter(a1)
        v2 = []
        for v3, v4 in v1.items():
            heapq.heappush(v2, MinHeapObj((v4, v3)))
            if len(v2) == a2 + 1:
                heapq.heappop(v2)
        v5 = []
        while v2:
            v5.append(heapq.heappop(v2).val[1])
        return v5[::-1]
