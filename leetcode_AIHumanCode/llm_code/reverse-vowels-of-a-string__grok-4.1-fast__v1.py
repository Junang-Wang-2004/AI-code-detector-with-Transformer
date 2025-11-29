class Solution:
    def reverseVowels(self, word):
        is_vowel = set('aeiouAEIOU')
        parts = list(word)
        rev_vowels = []
        for ch in word:
            if ch in is_vowel:
                rev_vowels.append(ch)
        rev_vowels.reverse()
        vowel_idx = 0
        for k in range(len(parts)):
            if parts[k] in is_vowel:
                parts[k] = rev_vowels[vowel_idx]
                vowel_idx += 1
        return ''.join(parts)
