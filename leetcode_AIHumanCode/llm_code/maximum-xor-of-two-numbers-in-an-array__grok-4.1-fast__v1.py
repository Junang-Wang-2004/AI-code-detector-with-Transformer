class Solution:
    def findMaximumXOR(self, nums):
        if not nums:
            return 0
        bits = max(n.bit_length() for n in nums)

        class Node:
            def __init__(self):
                self.children = [None] * 2

        root = Node()

        def insert(value):
            current = root
            for j in range(bits - 1, -1, -1):
                b = (value >> j) & 1
                if current.children[b] is None:
                    current.children[b] = Node()
                current = current.children[b]

        def search(value):
            current = root
            xor_val = 0
            for j in range(bits - 1, -1, -1):
                b = (value >> j) & 1
                opp_bit = 1 - b
                if current.children[opp_bit]:
                    xor_val |= (1 << j)
                    current = current.children[opp_bit]
                elif current.children[b]:
                    current = current.children[b]
                else:
                    return 0
            return xor_val

        best = 0
        for val in nums:
            best = max(best, search(val))
            insert(val)
        return best
