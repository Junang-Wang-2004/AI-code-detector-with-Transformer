import collections


class TrieNode:
    def __init__(self):
        self.children = {}
        self.failure = None
        self.word_ids = []
        self.match_ids = []


class ACBuilder:
    def __init__(self, word_list):
        self.root = TrieNode()
        self.populate_trie(word_list)
        self.setup_failures()

    def populate_trie(self, word_list):
        for wid, pat in enumerate(word_list):
            active = self.root
            for char in pat:
                if char not in active.children:
                    active.children[char] = TrieNode()
                active = active.children[char]
            active.word_ids.append(wid)

    def setup_failures(self):
        queue = collections.deque()
        self.root.failure = self.root
        self.root.match_ids = []
        for next_node in list(self.root.children.values()):
            next_node.failure = self.root
            queue.append(next_node)
        while queue:
            current = queue.popleft()
            current.match_ids = current.word_ids[:] + current.failure.match_ids
            for char, next_node in current.children.items():
                fail_ptr = current.failure
                while fail_ptr != self.root and char not in fail_ptr.children:
                    fail_ptr = fail_ptr.failure
                next_node.failure = fail_ptr.children.get(char, self.root)
                queue.append(next_node)


class Solution:
    def indexPairs(self, text, words):
        if not words:
            return []
        ac = ACBuilder(words)
        matches = []
        state = ac.root
        for pos in range(len(text)):
            ch = text[pos]
            while state != ac.root and ch not in state.children:
                state = state.failure
            state = state.children.get(ch, ac.root)
            for wid in state.match_ids:
                wlen = len(words[wid])
                begin = pos - wlen + 1
                matches.append([begin, pos])
        return sorted(matches)
