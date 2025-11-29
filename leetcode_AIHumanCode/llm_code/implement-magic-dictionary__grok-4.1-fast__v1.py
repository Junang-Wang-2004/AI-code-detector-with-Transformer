class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary):
        for term in dictionary:
            current = self.root
            for char in term:
                index = ord(char) - ord('a')
                if current.children[index] is None:
                    current.children[index] = TrieNode()
                current = current.children[index]
            current.is_end = True

    def search(self, target):
        def explore(pos, node, modified):
            if pos == len(target):
                return node.is_end and modified

            outcome = False
            char_index = ord(target[pos]) - ord('a')

            if node.children[char_index] is not None:
                if modified:
                    outcome = outcome or explore(pos + 1, node.children[char_index], True)
                else:
                    outcome = outcome or explore(pos + 1, node.children[char_index], False)

            if not modified:
                for alt in range(26):
                    if alt != char_index and node.children[alt] is not None:
                        outcome = outcome or explore(pos + 1, node.children[alt], True)

            return outcome

        return explore(0, self.root, False)
