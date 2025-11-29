import collections


class Node:
    def __init__(self):
        self.children = {}
        self.candidates = []

    def update(self, sentence, freq):
        for i, (negf, s) in enumerate(self.candidates):
            if s == sentence:
                self.candidates[i] = (-freq, sentence)
                break
        else:
            self.candidates.append((-freq, sentence))
        self.candidates.sort()
        self.candidates = self.candidates[:3]

    def insert(self, sentence, freq):
        curr = self
        curr.update(sentence, freq)
        for ch in sentence:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
            curr.update(sentence, freq)


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = Node()
        self.counts = collections.Counter()
        self.curr_node = self.root
        self.typed = []
        for sent, cnt in zip(sentences, times):
            self.counts[sent] = cnt
            self.root.insert(sent, cnt)

    def input(self, ch):
        if ch == '#':
            complete = ''.join(self.typed)
            self.counts[complete] += 1
            self.root.insert(complete, self.counts[complete])
            self.curr_node = self.root
            self.typed.clear()
            return []
        self.typed.append(ch)
        if self.curr_node is None:
            return []
        if ch not in self.curr_node.children:
            self.curr_node = None
            return []
        self.curr_node = self.curr_node.children[ch]
        return [s for _, s in self.curr_node.candidates]
