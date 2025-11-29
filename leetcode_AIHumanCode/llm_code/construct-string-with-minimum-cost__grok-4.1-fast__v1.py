class TrieNode:
    def __init__(self):
        self.children = {}
        self.cost = float('inf')

class Solution:
    def minimumCost(self, target, words, costs):
        root = TrieNode()
        for word, c in zip(words, costs):
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.cost = min(node.cost, c)
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for start in range(n):
            if dp[start] == float('inf'):
                continue
            node = root
            for pos in range(start, n):
                ch = target[pos]
                if ch not in node.children:
                    break
                node = node.children[ch]
                dp[pos + 1] = min(dp[pos + 1], dp[start] + node.cost)
        return dp[n] if dp[n] != float('inf') else -1
