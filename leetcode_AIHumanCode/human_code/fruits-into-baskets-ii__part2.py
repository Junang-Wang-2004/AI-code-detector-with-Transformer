# Time:  O(n^2)
# Space: O(1)
# brute force
class Solution2(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        """
        result = 0
        for x in fruits:
            i = next((i for i in range(len(baskets)) if baskets[i] >= x), -1)
            if i ==-1:
                result += 1
            else:
                baskets[i] = 0
        return result
