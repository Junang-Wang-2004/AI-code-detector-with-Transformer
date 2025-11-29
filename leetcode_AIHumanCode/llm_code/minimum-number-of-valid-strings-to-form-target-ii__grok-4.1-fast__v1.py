class Solution:
    def minValidStrings(self, words, target):
        class TrieNode:
            def __init__(self):
                self.children = [None] * 26

        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                i = ord(ch) - ord('a')
                if curr.children[i] is None:
                    curr.children[i] = TrieNode()
                curr = curr.children[i]

        idx = 0
        length = len(target)
        result = 0
        while idx < length:
            curr = root
            prev = idx
            while idx < length:
                i = ord(target[idx]) - ord('a')
                if curr.children[i] is None:
                    break
                curr = curr.children[i]
                idx += 1
            if idx == prev:
                return -1
            result += 1
        return result
