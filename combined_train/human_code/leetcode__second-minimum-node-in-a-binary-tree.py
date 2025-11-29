import heapq

class C1(object):

    def findSecondMinimumValue(self, a1):
        """
        """

        def findSecondMinimumValueHelper(a1, a2, a3):
            if not a1:
                return
            if a1.val not in a3:
                heapq.heappush(a2, -a1.val)
                a3.add(a1.val)
                if len(a2) > 2:
                    a3.remove(-heapq.heappop(a2))
            findSecondMinimumValueHelper(a1.left, a2, a3)
            findSecondMinimumValueHelper(a1.right, a2, a3)
        v1, v2 = ([], set())
        findSecondMinimumValueHelper(a1, v1, v2)
        if len(v1) < 2:
            return -1
        return -v1[0]
