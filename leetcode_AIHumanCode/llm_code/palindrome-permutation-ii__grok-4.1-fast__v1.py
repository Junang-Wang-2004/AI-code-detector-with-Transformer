import collections

class Solution:
    def generatePalindromes(self, s):
        freq = collections.Counter(s)
        odd_chars = [char for char in freq if freq[char] % 2 == 1]
        if len(odd_chars) > 1:
            return []
        center = odd_chars[0] if odd_chars else ''
        side_freq = {char: freq[char] // 2 for char in freq}
        half_length = sum(side_freq.values())
        result = []
        def build_path(path):
            if len(path) == half_length:
                prefix = ''.join(path)
                result.append(prefix + center + prefix[::-1])
                return
            for char in sorted(side_freq):
                if side_freq[char] > 0:
                    side_freq[char] -= 1
                    path.append(char)
                    build_path(path)
                    path.pop()
                    side_freq[char] += 1
        build_path([])
        return result
