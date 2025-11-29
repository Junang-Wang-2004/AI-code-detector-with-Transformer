# Time:  O(nlogk)
# Space: O(nlogk)
# binary lifting
class Solution2(object):
    def getMaxFunctionValue(self, receiver, k):
        """
        """
        l = (k+1).bit_length()
        P = [receiver[:] for _ in range(l)]
        S = [list(range(len(receiver))) for _ in range(l)]
        for i in range(1, len(P)):
            for u in range(len(receiver)):
                P[i][u] = P[i-1][P[i-1][u]]
                S[i][u] = S[i-1][u]+S[i-1][P[i-1][u]]
        result = 0
        for u in range(len(receiver)):
            curr = 0
            for i in range(l):
                if (k+1)&(1<<i):
                    curr += S[i][u]
                    u = P[i][u]
            result = max(result, curr)
        return result
