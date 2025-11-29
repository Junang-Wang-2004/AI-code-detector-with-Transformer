# Time:  O(logf)
# Space: O(1)

# math, combinatorics
class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        """
        def count(x):
            def length(x):
                result = 0
                while x:
                    x //= 10
                    result += 1
                return result

            result = 0
            n = length(x)
            base = 10**n
            l = n-len(s)
            cnt = (limit+1)**l
            for i in range(l):
                base //= 10
                curr = x//base%10
                cnt //= limit+1
                result += (min(curr-1, limit)-0+1)*cnt
                if curr > limit:
                    break
            else:
                if x%base >= int(s):
                    result += 1
            return result

        return count(finish)-count(start-1)


