class Solution:
    def sortVowels(self, s: str) -> str:
        vow_set = set('aeiouAEIOU')
        vow_chars = [ch for ch in s if ch in vow_set]
        vow_chars.sort()
        result = []
        idx = 0
        for ch in s:
            if ch in vow_set:
                result.append(vow_chars[idx])
                idx += 1
            else:
                result.append(ch)
        return ''.join(result)
