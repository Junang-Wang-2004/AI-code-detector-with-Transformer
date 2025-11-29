class Solution:
    def findWords(self, board_lines):
        lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        return [w for w in board_lines if any(set(w.lower()) <= set(line) for line in lines)]
