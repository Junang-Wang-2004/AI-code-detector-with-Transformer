class Solution:
    def mostCommonWord(self, paragraph, banned):
        forbidden = set(banned)
        frequency = {}
        for token in paragraph.lower().split():
            purified = ''.join(character for character in token if character.isalpha())
            if purified and purified not in forbidden:
                frequency[purified] = frequency.get(purified, 0) + 1
        return max(frequency, key=frequency.get)
