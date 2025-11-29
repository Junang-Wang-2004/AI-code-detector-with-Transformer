class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current['end'] = True

    def search(self, word):
        stack = [(0, self.root)]
        while stack:
            index, node = stack.pop()
            if index == len(word):
                return node.get('end', False)
            char = word[index]
            if char == '.':
                for key in node:
                    if key != 'end':
                        stack.append((index + 1, node[key]))
            else:
                if char in node:
                    stack.append((index + 1, node[char]))
        return False
