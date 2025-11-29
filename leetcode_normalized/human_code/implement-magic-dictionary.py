import collections

class C1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        v1 = lambda: collections.defaultdict(v1)
        self.trie = v1()

    def buildDict(self, a1):
        """
        Build a dictionary through a list of words
        """
        for v1 in a1:
            reduce(dict.__getitem__, v1, self.trie).setdefault('_end')

    def search(self, a1):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """

        def find(a1, a2, a3, a4):
            if a3 == len(a1):
                return '_end' in a2 and (not a4)
            if a1[a3] not in a2:
                return any((find(a1, a2[c], a3 + 1, False) for v1 in a2 if v1 != '_end')) if a4 else False
            if a4:
                return find(a1, a2[a1[a3]], a3 + 1, True) or any((find(a1, a2[v1], a3 + 1, False) for v1 in a2 if v1 not in ('_end', a1[a3])))
            return find(a1, a2[a1[a3]], a3 + 1, False)
        return find(a1, self.trie, 0, True)
