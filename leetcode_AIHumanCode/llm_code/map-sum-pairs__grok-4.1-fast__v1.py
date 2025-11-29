class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal_value = 0
        self.subtree_sum = 0


class MapSum:
    def __init__(self):
        self.root_node = TrieNode()

    def insert(self, key, value):
        current = self.root_node
        traversal = [current]
        for letter in key:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
            traversal.append(current)
        change = value - current.terminal_value
        current.terminal_value = value
        for position in traversal:
            position.subtree_sum += change

    def sum(self, prefix):
        current = self.root_node
        for letter in prefix:
            if letter not in current.children:
                return 0
            current = current.children[letter]
        return current.subtree_sum
