class C1(object):

    def knightDialer(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        v3 = [[1 for v4 in range(10)] for v4 in range(2)]
        for v5 in range(a1 - 1):
            v3[(v5 + 1) % 2] = [0] * 10
            for v6 in range(10):
                for v7 in v2[v6]:
                    v3[(v5 + 1) % 2][v7] += v3[v5 % 2][v6]
                    v3[(v5 + 1) % 2][v7] %= v1
        return sum(v3[(a1 - 1) % 2]) % v1
