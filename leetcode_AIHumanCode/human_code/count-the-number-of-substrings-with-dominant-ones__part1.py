# Time:  O(n * sqrt(n)) = O(n^(3/2))
# Space: O(n)

# two pointers, sliding window
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        """
        result = 0
        idxs = [-1]+[i for i, x in enumerate(s) if x == '0']+[len(s)]
        curr = 1
        for i in range(len(s)):
            if idxs[curr] == i:
                curr += 1
            for c in range(min(int((-1+(1+4*(i+1))**0.5)/2)+1, curr)):  # since c^2 <= (i+1)-c, thus c <= (-1+(1+4*(i+1))**0.5)/2
                if c**2 <= (i-idxs[(curr-c)-1])-c:
                    result += min(min(idxs[curr-c], i)-idxs[(curr-c)-1], ((i-idxs[(curr-c)-1])-c)-c**2+1)
        return result


