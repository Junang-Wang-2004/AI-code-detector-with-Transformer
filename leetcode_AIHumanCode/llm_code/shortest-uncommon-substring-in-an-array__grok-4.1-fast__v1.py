class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def update(self, s, delta):
        for start in range(len(s)):
            curr = self.root
            for pos in range(start, len(s)):
                ch = s[pos]
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
                curr.count += delta

    def shortest_unique(self, s):
        best = (float('inf'), "")
        for begin in range(len(s)):
            curr = self.root
            for end in range(begin, len(s)):
                ch = s[end]
                curr = curr.children[ch]
                ln = end - begin + 1
                if curr.count == 0:
                    cand = (ln, s[begin:end + 1])
                    if cand < best:
                        best = cand
                    break
        return best[1]

class Solution:
    def shortestSubstrings(self, arr):
        tree = Trie()
        for word in arr:
            tree.update(word, 1)
        output = []
        for word in arr:
            tree.update(word, -1)
            output.append(tree.shortest_unique(word))
            tree.update(word, 1)
        return output
