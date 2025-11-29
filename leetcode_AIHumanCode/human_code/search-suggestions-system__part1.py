# Time:  ctor: O(n * l), n is the number of products
#                      , l is the average length of product name
#        suggest: O(l^2)
# Space: O(t), t is the number of nodes in trie

import collections


class TrieNode(object):

    def __init__(self):
        self.__TOP_COUNT = 3
        self.leaves = collections.defaultdict(TrieNode)
        self.infos = []

    def insert(self, words, i):
        curr = self
        for c in words[i]:
            curr = curr.leaves[c]
            curr.add_info(words, i)

    def add_info(self, words, i):
        self.infos.append(i)
        self.infos.sort(key=lambda x: words[x])
        if len(self.infos) > self.__TOP_COUNT:
            self.infos.pop()


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        """
        trie = TrieNode()
        for i in range(len(products)):
            trie.insert(products, i)
        result = [[] for _ in range(len(searchWord))]
        for i, c in enumerate(searchWord):
            if c not in trie.leaves:
                break
            trie = trie.leaves[c]
            result[i] = [products[x] for x in trie.infos]
        return result


