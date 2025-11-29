# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def checkPartitioning(self, s):
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
        prefix, suffix = [], []
        for i in range(2, len(P)-2):
            if i-1-P[i] == 0:
                prefix.append(i)
            if i+1+P[i] == len(P)-1:
                suffix.append(i)
        for i in prefix:
            for j in suffix:
                left, right = i+1+P[i], j-1-P[j]
                if left > right:
                    continue
                mid = left + (right-left)//2
                if P[mid] >= mid-left:
                    return True
        return False


