class Solution:
    def minimumCost(self, target, words, costs):
        INF = float('inf')
        n = len(target)
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.minc = INF
        root = TrieNode()
        num_words = len(words)
        for idx in range(num_words):
            curr = root
            wrd = words[idx]
            cst = costs[idx]
            for ch in wrd:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.minc = min(curr.minc, cst)
        dist = [INF] * (n + 1)
        dist[0] = 0
        for begin in range(n):
            if dist[begin] == INF:
                continue
            curr = root
            for idx in range(begin, n):
                ch = target[idx]
                if ch not in curr.children:
                    break
                curr = curr.children[ch]
                if curr.minc != INF:
                    dist[idx + 1] = min(dist[idx + 1], dist[begin] + curr.minc)
        return dist[n] if dist[n] != INF else -1
