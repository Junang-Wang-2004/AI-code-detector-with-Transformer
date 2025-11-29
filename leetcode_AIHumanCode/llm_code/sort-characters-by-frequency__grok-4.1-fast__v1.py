class Solution(object):
    def frequencySort(self, s):
        tally = {}
        for letter in s:
            tally[letter] = tally.get(letter, 0) + 1
        chars = sorted(tally, key=tally.get, reverse=True)
        return ''.join(letter * tally[letter] for letter in chars)
