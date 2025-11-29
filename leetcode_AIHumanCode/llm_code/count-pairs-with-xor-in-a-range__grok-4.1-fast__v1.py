class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, val):
        cur = self.root
        for k in range(31, -1, -1):
            b = (val >> k) & 1
            if cur.children[b] is None:
                cur.children[b] = TrieNode()
            cur = cur.children[b]
            cur.count += 1

    def query(self, val, cap):
        if cap < 0:
            return 0
        cur = self.root
        total = 0
        for k in range(31, -1, -1):
            if cur is None:
                return total
            b_val = (val >> k) & 1
            b_cap = (cap >> k) & 1
            if b_cap == 1:
                if cur.children[b_val]:
                    total += cur.children[b_val].count
                nxt_b = 1 ^ b_val
                if cur.children[nxt_b] is None:
                    return total
                cur = cur.children[nxt_b]
            else:
                nxt_b = b_val
                if cur.children[nxt_b] is None:
                    return total
                cur = cur.children[nxt_b]
        return total

class Solution:
    def countPairs(self, nums, low, high):
        tree = Trie()
        answer = 0
        for val in nums:
            answer += tree.query(val, high + 1) - tree.query(val, low)
            tree.insert(val)
        return answer
