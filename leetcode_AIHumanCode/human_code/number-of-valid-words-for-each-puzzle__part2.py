# Time:  O(m*2^(L-1) + n*(l+m)), m is the number of puzzles, L is the length of puzzles
#                              , n is the number of words, l is the max length of words
# Space: O(m*2^(L-1))
import collections
from functools import reduce


class Solution2(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        """
        L = 7
        lookup = collections.defaultdict(list)
        for i in range(len(puzzles)):
            bits = []
            base = 1 << (ord(puzzles[i][0])-ord('a'))
            for j in range(1, L):
                bits.append(ord(puzzles[i][j])-ord('a'))
            for k in range(2**len(bits)):
                bitset = base
                for j in range(len(bits)):
                    if k & (1<<j):
                        bitset |= 1<<bits[j]
                lookup[bitset].append(i)
        result = [0]*len(puzzles)
        for word in words:
            bitset = 0
            for c in word:
                bitset |= 1<<(ord(c)-ord('a'))
            if bitset not in lookup:
                continue
            for i in lookup[bitset]:
                result[i] += 1
        return result
