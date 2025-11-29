# Time:  O(logf)
# Space: O(logf)
# math, combinatorics
class Solution2(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        """
        def count(x):
            result = 0
            str_x = str(x)
            l = len(str_x)-len(s)
            cnt = (limit+1)**l
            for i in range(l):
                cnt //= limit+1
                result += (min(int(str_x[i])-1, limit)-0+1)*cnt
                if int(str_x[i]) > limit:
                    break
            else:
                if int(str_x[-len(s):]) >= int(s):
                    result += 1
            return result

        return count(finish)-count(start-1)
