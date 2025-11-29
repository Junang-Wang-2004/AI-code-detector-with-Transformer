# Time:  O(n * sqrt(n)) = O(n^(3/2))
# Space: O(n)
# two pointers, sliding window
class Solution2(object):
    def numberOfSubstrings(self, s):
        """
        """
        result = 0
        idxs = [-1]+[i for i, x in enumerate(s) if x == '0']+[len(s)]
        for c in range(int((-1+(1+4*len(s))**0.5)/2)+1):  # since c^2 <= n-c, thus c <= (-1+(1+4*n)**0.5)/2
            left = right = 1
            for i in range(len(s)):
                if idxs[right] == i:
                    right += 1
                if right-left == c+1:
                    left += 1
                if not (right-left == c and ((i-idxs[left-1])-c) >= c**2):
                    continue
                result += min(min(idxs[left], i)-idxs[left-1], ((i-idxs[left-1])-c)-c**2+1)
        return result


