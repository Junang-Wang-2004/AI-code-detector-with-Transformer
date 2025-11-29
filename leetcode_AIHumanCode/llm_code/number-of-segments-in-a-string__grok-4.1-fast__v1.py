class Solution:
    def countSegments(self, s):
        count = 0
        is_prev_space = True
        for char in s:
            if char != ' ':
                if is_prev_space:
                    count += 1
                is_prev_space = False
            else:
                is_prev_space = True
        return count
