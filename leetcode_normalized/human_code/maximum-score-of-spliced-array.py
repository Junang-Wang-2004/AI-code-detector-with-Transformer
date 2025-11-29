class C1(object):

    def maximumsSplicedArray(self, a1, a2):
        """
        """

        def kadane(a1):
            v1 = v2 = 0
            for v3 in a1:
                v2 = max(v2 + v3, 0)
                v1 = max(v1, v2)
            return v1
        return max(sum(a1) + kadane((a2[i] - a1[i] for v1 in range(len(a1)))), sum(a2) + kadane((a1[v1] - a2[v1] for v1 in range(len(a2)))))
