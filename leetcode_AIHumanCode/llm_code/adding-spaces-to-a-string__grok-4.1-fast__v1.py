class Solution(object):
    def addSpaces(self, text, positions):
        chars = []
        pos_idx = 0
        count_pos = len(positions)
        for i, ch in enumerate(text):
            while pos_idx < count_pos and positions[pos_idx] == i:
                chars.append(' ')
                pos_idx += 1
            chars.append(ch)
        return ''.join(chars)
