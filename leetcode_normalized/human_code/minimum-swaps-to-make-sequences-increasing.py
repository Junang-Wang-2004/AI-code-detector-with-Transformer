class C1(object):

    def minSwap(self, a1, a2):
        """
        """
        v1, v2 = ([0] * 2, [1] * 2)
        for v3 in range(1, len(a1)):
            v1[v3 % 2], v2[v3 % 2] = (float('inf'), float('inf'))
            if a1[v3 - 1] < a1[v3] and a2[v3 - 1] < a2[v3]:
                v1[v3 % 2] = min(v1[v3 % 2], v1[(v3 - 1) % 2])
                v2[v3 % 2] = min(v2[v3 % 2], v2[(v3 - 1) % 2] + 1)
            if a1[v3 - 1] < a2[v3] and a2[v3 - 1] < a1[v3]:
                v1[v3 % 2] = min(v1[v3 % 2], v2[(v3 - 1) % 2])
                v2[v3 % 2] = min(v2[v3 % 2], v1[(v3 - 1) % 2] + 1)
        return min(v1[(len(a1) - 1) % 2], v2[(len(a1) - 1) % 2])
