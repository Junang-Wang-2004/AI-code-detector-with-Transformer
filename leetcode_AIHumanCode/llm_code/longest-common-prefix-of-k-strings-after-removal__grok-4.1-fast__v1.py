class TrieNode:
    def __init__(self):
        self.children = {}
        self.pass_count = 0
        self.best = 0

class Solution:
    def longestCommonPrefix(self, strs, kk):
        root = TrieNode()
        def traverse_update(s, delta):
            nodes = [root]
            cur = root
            for ch in s:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
                nodes.append(cur)
            for dep in range(len(s), -1, -1):
                nd = nodes[dep]
                nd.pass_count += delta
                nd.best = dep if nd.pass_count >= kk else 0
                for nxt in nd.children.values():
                    nd.best = max(nd.best, nxt.best)

        n = len(strs)
        ans = [0] * n
        for s in strs:
            traverse_update(s, 1)
        for i in range(n):
            traverse_update(strs[i], -1)
            ans[i] = root.best
            traverse_update(strs[i], 1)
        return ans
