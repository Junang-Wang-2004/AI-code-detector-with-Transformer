class Solution:
    def longestValidSubstring(self, word, forbidden):
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False

        root = TrieNode()
        for s in forbidden:
            curr = root
            for c in s:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_end = True

        length = len(word)
        maximum = 0
        end = length - 1
        for start in range(length - 1, -1, -1):
            curr = root
            for idx in range(start, end + 1):
                ch = word[idx]
                if ch not in curr.children:
                    break
                curr = curr.children[ch]
                if curr.is_end:
                    end = idx - 1
                    break
            maximum = max(maximum, end - start + 1)
        return maximum
