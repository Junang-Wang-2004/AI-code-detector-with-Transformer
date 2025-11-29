# Time:  ctor: O(n * l * log(n * l)), n is the number of products
#                                   , l is the average length of product name
#        suggest: O(l^2)
# Space: O(t), t is the number of nodes in trie
class TrieNode2(object):

    def __init__(self):
        self.__TOP_COUNT = 3
        self.leaves = collections.defaultdict(TrieNode2)
        self.infos = []

    def insert(self, words, i):
        curr = self
        for c in words[i]:
            curr = curr.leaves[c]
            curr.add_info(i)

    def add_info(self, i):
        if len(self.infos) == self.__TOP_COUNT:
            return
        self.infos.append(i)


class Solution2(object):
    def suggestedProducts(self, products, searchWord):
        """
        """
        products.sort()
        trie = TrieNode2()
        for i in range(len(products)):
            trie.insert(products, i)
        result = [[] for _ in range(len(searchWord))]
        for i, c in enumerate(searchWord):
            if c not in trie.leaves:
                break
            trie = trie.leaves[c]
            result[i] = [products[x] for x in trie.infos]
        return result


