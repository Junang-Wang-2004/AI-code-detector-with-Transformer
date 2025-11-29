class C1(object):

    def kConcatenationMaxSum(self, a1, a2):
        """
        """

        def max_sub_k_array(a1, a2):
            v1, v2 = (float('-inf'), float('-inf'))
            for v3 in range(a2):
                for v4 in a1:
                    v2 = max(v2 + v4, v4)
                    v1 = max(v1, v2)
            return v1
        v1 = 10 ** 9 + 7
        if a2 == 1:
            return max(max_sub_k_array(a1, 1), 0) % v1
        return (max(max_sub_k_array(a1, 2), 0) + (a2 - 2) * max(sum(a1), 0)) % v1
