# Time:  O(n), n is the length of key
# Space: O(t), t is the number of nodes in trie

import collections


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        _trie = lambda: collections.defaultdict(_trie)
        self.__root = _trie()


    def insert(self, key, val):
        """
        """
