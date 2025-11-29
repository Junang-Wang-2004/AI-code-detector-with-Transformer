# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def maxProduct(self, s):
        """
        """
        def manacher(s):
            s = '^#' + '#'.join(s) + '#$'
            P = [0]*len(s)
            C, R = 0, 0
            for i in range(1, len(s)-1):
                i_mirror = 2*C-i
                if R > i:
                    P[i] = min(R-i, P[i_mirror])
                while s[i+1+P[i]] == s[i-1-P[i]]:
                    P[i] += 1
                if i+P[i] > R:
                    C, R = i, i+P[i]
            return P

        P = manacher(s)
        q = collections.deque()
        left = [0]
        for i in range(len(s)):
            while q and q[0][1] < i:
                q.popleft()
            left.append(max(left[-1], 1+2*(i-q[0][0]) if q else 1))
            q.append((i, i+P[2*i+2]//2))
        q = collections.deque()
        result = right = 0
        for i in reversed(range(len(s))):
            while q and q[0][1] > i:
                q.popleft()
            right = max(right, 1+2*(q[0][0]-i) if q else 1)
            q.append((i, i-P[2*i+2]//2))
            result = max(result, left[i]*right)
        return result


