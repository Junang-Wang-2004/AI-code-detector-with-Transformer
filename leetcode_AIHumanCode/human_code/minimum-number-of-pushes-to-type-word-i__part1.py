# Time:  O(4)
# Space: O(1)

# greedy
class Solution(object):
    def minimumPushes(self, word):
        """
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        return sum((i+1)*min(len(word)-i*(9-2+1), (9-2+1)) for i in range(ceil_divide(len(word), (9-2+1))))


