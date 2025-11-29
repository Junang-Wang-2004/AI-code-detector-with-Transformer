from collections import defaultdict

class Node:
    def __init__(self):
        self.children = [None] * 2
        self.count = 0

class XorTrie:
    def __init__(self, bits):
        self.bits = bits
        self.root = Node()

    def insert(self, num, delta):
        node = self.root
        node.count += delta
        for i in range(self.bits - 1, -1, -1):
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = Node()
            node = node.children[bit]
            node.count += delta

    def get_max_xor(self, num):
        node = self.root
        if node.count == 0:
            return 0
        res = 0
        for i in range(self.bits - 1, -1, -1):
            bit = (num >> i) & 1
            opp = 1 - bit
            if node.children[opp] is not None and node.children[opp].count > 0:
                res |= (1 << i)
                node = node.children[opp]
            elif node.children[bit] is not None and node.children[bit].count > 0:
                node = node.children[bit]
            else:
                break
        return res

class Solution:
    def maxGeneticDifference(self, parents, queries):
        n = len(parents)
        tree = defaultdict(list)
        root = next(i for i, p in enumerate(parents) if p == -1)
        for i, p in enumerate(parents):
            if p != -1:
                tree[p].append(i)
        query_groups = defaultdict(list)
        max_val = n - 1
        for idx, (nd, val) in enumerate(queries):
            query_groups[nd].append((idx, val))
            if val > max_val:
                max_val = val
        bits = (max_val).bit_length()
        ans = [0] * len(queries)
        trie = XorTrie(bits)
        stack = [(0, root)]
        while stack:
            phase, u = stack[-1]
            if phase == 0:
                stack[-1] = (1, u)
                trie.insert(u, 1)
                for qid, val in query_groups[u]:
                    ans[qid] = trie.get_max_xor(val)
                for child in reversed(tree[u]):
                    stack.append((0, child))
            else:
                trie.insert(u, -1)
                stack.pop()
        return ans
