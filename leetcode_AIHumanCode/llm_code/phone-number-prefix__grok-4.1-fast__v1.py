class Solution:
    def phonePrefix(self, numbers):
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False

        root = TrieNode()

        def insert(num):
            curr = root
            for digit in num:
                if curr.is_end:
                    return False
                d = int(digit)
                if d not in curr.children:
                    curr.children[d] = TrieNode()
                curr = curr.children[d]
            if curr.is_end or curr.children:
                return False
            curr.is_end = True
            return True

        for num in numbers:
            if not insert(num):
                return False
        return True
