from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, W):
        if len(hand) % W != 0:
            return False
        freq = Counter(hand)
        uniques = sorted(freq)
        num_groups = len(hand) // W
        for _ in range(num_groups):
            pos = 0
            while pos < len(uniques) and freq[uniques[pos]] == 0:
                pos += 1
            if pos == len(uniques):
                return False
            seq_start = uniques[pos]
            val = seq_start
            for _ in range(W):
                if freq[val] == 0:
                    return False
                freq[val] -= 1
                val += 1
        return True
