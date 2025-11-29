class C1(object):

    def minPathSum(self, a1):
        sum = list(a1[0])
        for v1 in range(1, len(a1[0])):
            sum[v1] = sum[v1 - 1] + a1[0][v1]
        for v2 in range(1, len(a1)):
            sum[0] += a1[v2][0]
            for v1 in range(1, len(a1[0])):
                sum[v1] = min(sum[v1 - 1], sum[v1]) + a1[v2][v1]
        return sum[-1]
