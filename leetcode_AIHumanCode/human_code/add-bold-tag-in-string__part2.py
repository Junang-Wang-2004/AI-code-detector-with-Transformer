# Time:  O(n * l), l is the average string length
# Space: O(t)    , t is the size of trie
# trie solution, 439ms
class Solution2(object):
    def addBoldTag(self, s, words):
        """
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for i, word in enumerate(words):
            functools.reduce(dict.__getitem__, word, trie).setdefault("_end")

        lookup = [False] * len(s)
        for i in range(len(s)):
            curr = trie
            k = -1
            for j in range(i, len(s)):
                if s[j] not in curr:
                    break
                curr = curr[s[j]]
                if "_end" in curr:
                    k = j
            for j in range(i, k+1):
                lookup[j] = True

        result = []
        for i in range(len(s)):
            if lookup[i] and (i == 0 or not lookup[i-1]):
                result.append("<b>")
            result.append(s[i])
            if lookup[i] and (i == len(s)-1 or not lookup[i+1]):
                result.append("</b>")
        return "".join(result)

