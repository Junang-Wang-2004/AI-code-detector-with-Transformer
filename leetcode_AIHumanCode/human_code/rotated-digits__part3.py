# Time:  O(nlogn) = O(n), because O(logn) = O(32) by this input
# Space: O(logn) = O(1)
class Solution3(object):
    def rotatedDigits(self, N):
        """
        """
        invalid, diff = set(['3', '4', '7']), set(['2', '5', '6', '9'])
        result = 0
        for i in range(N+1):
            lookup = set(list(str(i)))
            if invalid & lookup:
                continue
            if diff & lookup:
                result += 1
        return result


