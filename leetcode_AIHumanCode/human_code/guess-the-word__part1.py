# Time:  O(n)
# Space: O(n)

import collections
import itertools


class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        """
        possible = list(range(len(wordlist)))
        n = 0
        while n < 6:
            count = [collections.Counter(w[i] for w in wordlist) for i in range(6)]
            guess = max(possible, key=lambda x: sum(count[i][c] for i, c in enumerate(wordlist[x])))
            n = master.guess(wordlist[guess])
            possible = [j for j in possible if sum(a == b for a, b in zip(wordlist[guess], wordlist[j])) == n]


