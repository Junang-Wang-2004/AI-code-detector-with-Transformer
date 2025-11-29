# Time:  O(n * sqrt(n)) = O(n^(3/2))
# Space: O(1)
# two pointers, sliding window
class Solution_TLE(object):
    def numberOfSubstrings(self, s):
        """
        """
        result = 0
        for c in range(int((-1+(1+4*len(s))**0.5)/2)+1):  # since c^2 <= n-c, thus c <= (-1+(1+4*n)**0.5)/2
            cnt = [0]*2
            left = curr = 0
            for right in range(len(s)):
                cnt[s[right] == '1'] += 1
                while cnt[0] == c+1:
                    cnt[s[left] == '1'] -= 1
                    left += 1
                if not (cnt[0] == c and cnt[1] >= c**2):
                    continue
                for curr in range(max(curr, left), right):
                    if s[curr] == '0':
                        break
                else:
                    curr = right
                result += min(curr-left+1, cnt[1]-c**2+1)
        return result
