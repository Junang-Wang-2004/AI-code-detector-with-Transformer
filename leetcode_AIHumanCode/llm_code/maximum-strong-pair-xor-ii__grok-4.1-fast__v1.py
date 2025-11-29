class Solution:
    def maximumStrongPairXor(self, nums):
        nums.sort()
        class TrieNode:
            def __init__(self):
                self.children = [None, None]
                self.count = 0

        root = TrieNode()

        def insert(node, val, delta):
            curr = node
            for k in range(31, -1, -1):
                bit = (val >> k) & 1
                if curr.children[bit] is None:
                    curr.children[bit] = TrieNode()
                curr = curr.children[bit]
                curr.count += delta

        def get_max_xor(node, val):
            curr = node
            xor_val = 0
            for k in range(31, -1, -1):
                bit = (val >> k) & 1
                opp_bit = 1 - bit
                if curr.children[opp_bit] and curr.children[opp_bit].count > 0:
                    xor_val |= (1 << k)
                    curr = curr.children[opp_bit]
                elif curr.children[bit] and curr.children[bit].count > 0:
                    curr = curr.children[bit]
                else:
                    break
            return xor_val

        max_res = 0
        l = 0
        for r in range(len(nums)):
            insert(root, nums[r], 1)
            while l <= r and nums[r] > 2 * nums[l]:
                insert(root, nums[l], -1)
                l += 1
            max_res = max(max_res, get_max_xor(root, nums[r]))
        return max_res
