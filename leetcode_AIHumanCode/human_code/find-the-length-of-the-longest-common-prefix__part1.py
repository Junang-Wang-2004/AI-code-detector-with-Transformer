from functools import reduce
# Time:  O((n + m) * l)
# Space: O(t)

# trie
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for x in arr1:
            reduce(dict.__getitem__, str(x), trie)
        result = 0
        for x in arr2:
            curr = trie
            for i, c in enumerate(str(x)):
                if c not in curr:
                    break
                curr = curr[c]
            else:
                i += 1
            result = max(result, i)
        return result


