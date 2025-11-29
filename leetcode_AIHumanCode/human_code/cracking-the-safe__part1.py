# Time:  O(k^n)
# Space: O(k^n)

class Solution(object):
    def crackSafe(self, n, k):
        """
        """
        M = k**(n-1)
        P = [q*k+i for i in range(k) for q in range(M)]  # rotate: i*k^(n-1) + q => q*k + i
        result = [str(k-1)]*(n-1)
        for i in range(k**n):
            j = i
            # concatenation in lexicographic order of Lyndon words
            while P[j] >= 0:
                result.append(str(j//M))
                P[j], j = -1, P[j]
        return "".join(result)


