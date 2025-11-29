# Time:  O(n * l), n is the length of S, l is the average length of words
# Space: O(t)    , t is the size of trie

import collections
import functools


class Solution(object):
    def boldWords(self, words, S):
        """
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for i, word in enumerate(words):
            functools.reduce(dict.__getitem__, word, trie).setdefault("_end")

        lookup = [False] * len(S)
        for i in range(len(S)):
            curr = trie
            k = -1
            for j in range(i, len(S)):
                if S[j] not in curr:
                    break
                curr = curr[S[j]]
                if "_end" in curr:
                    k = j
            for j in range(i, k+1):
                lookup[j] = True

        result = []
        for i in range(len(S)):
            if lookup[i] and (i == 0 or not lookup[i-1]):
                result.append("<b>")
            result.append(S[i])
            if lookup[i] and (i == len(S)-1 or not lookup[i+1]):
                result.append("</b>")
        return "".join(result)


