class Solution:
    def findRoot(self, tree):
        xor_all_nodes = 0
        xor_all_kids = 0
        for curr in tree:
            xor_all_nodes ^= id(curr)
        for curr in tree:
            for sub in curr.children:
                xor_all_kids ^= id(sub)
        target_id = xor_all_nodes ^ xor_all_kids
        for curr in tree:
            if id(curr) == target_id:
                return curr
        return None
