# Time:  ctor:   O(w * l^2), w is the number of words, l is the word length on average
#        search: O(p + s)  , p is the length of the prefix, s is the length of the suffix,
# Space: O(t), t is the number of trie nodes

import collections


class WordFilter(object):

    def __init__(self, words):
        """
        """
        _trie = lambda: collections.defaultdict(_trie)
        self.__trie = _trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.__trie
                cur["_weight"] = weight
                for j in range(i, 2*len(word)-1):
                    cur = cur[word[j%len(word)]]
                    cur["_weight"] = weight

    def f(self, prefix, suffix):
        """
        """
        cur = self.__trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur["_weight"]


