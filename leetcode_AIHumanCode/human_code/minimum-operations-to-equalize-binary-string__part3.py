# Time:  O(n)
# Space: O(1)
# math
class Solution3(object):
    def minOperations(self, s, k):
        """
        """
        zero = s.count('0')
        for i in range(len(s)+1):
            if (i*k-zero)&1:
                continue
            if i&1:
                if zero <= i*k <= zero*i+(len(s)-zero)*(i-1):
                    return i
            else:
                if zero <= i*k <= zero*(i-1)+(len(s)-zero)*i:
                    return i
        return -1
