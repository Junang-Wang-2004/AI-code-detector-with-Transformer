class Solution:
    def findTheLongestSubstring(self, s):
        vowels = 'aeiou'
        earliest = {0: -1}
        state = 0
        maximum = 0
        for idx, letter in enumerate(s):
            if letter in vowels:
                vowel_pos = vowels.index(letter)
                state ^= (1 << vowel_pos)
            if state in earliest:
                maximum = max(maximum, idx - earliest[state])
            else:
                earliest[state] = idx
        return maximum
