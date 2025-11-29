# Time:  O(n)
# Space: O(1)

# greedy, partition
class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        """
        a = list(s)
        left = 0
        for i in range(len(a)):
            if a[i] != '1':
                continue
            a[i], a[left] = a[left], a[i]
            left += 1
        if a[-1] != '1':
            a[-1], a[left-1] = a[left-1], a[-1]
        return "".join(a)


