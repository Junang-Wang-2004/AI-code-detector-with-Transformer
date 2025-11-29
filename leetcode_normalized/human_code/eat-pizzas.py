class C1(object):

    def maxWeight(self, a1):
        """
        """
        v1 = len(a1) // 4
        a1.sort(reverse=True)
        return sum((a1[i] for v2 in range((v1 + 1) // 2))) + sum((a1[v2] for v2 in range((v1 + 1) // 2 + 1, (v1 + 1) // 2 + 1 + v1 // 2 * 2, 2)))
