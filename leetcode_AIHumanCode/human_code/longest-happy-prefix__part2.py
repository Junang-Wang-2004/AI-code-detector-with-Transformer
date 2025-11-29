# Time:  O(n) on average
# Space: O(1)
# rolling-hash solution
class Solution2(object):
    def longestPrefix(self, s):
        """
        """
        M = 10**9+7
        D = 26
        def check(l, s):
            for i in range(l):
                if s[i] != s[len(s)-l+i]:
                    return False
            return True
    
        result, prefix, suffix, power = 0, 0, 0, 1
        for i in range(len(s)-1):
            prefix = (prefix*D + (ord(s[i])-ord('a'))) % M
            suffix = (suffix + (ord(s[len(s)-(i+1)])-ord('a'))*power) % M
            power = (power*D)%M
            if prefix == suffix:
                # we assume M is a very large prime without hash collision
                # assert(check(i+1, s))
                result = i+1
        return s[:result]
