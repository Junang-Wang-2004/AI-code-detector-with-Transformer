# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def lemonadeChange(self, bills):
        """
        """
        coins = [20, 10, 5]
        counts = collections.defaultdict(int)
        for bill in bills:
            counts[bill] += 1
            change = bill - coins[-1]
            for coin in coins:
                if change == 0:
                    break
                if change >= coin:
                    count = min(counts[coin], change//coin)
                    counts[coin] -= count
                    change -= coin * count
            if change != 0:
                return False
        return True


