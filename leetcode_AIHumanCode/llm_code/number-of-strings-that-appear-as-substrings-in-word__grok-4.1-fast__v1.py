class Solution:
    def numOfStrings(self, patterns, word):
        result = 0
        w_length = len(word)
        for substr in patterns:
            s_length = len(substr)
            if s_length > w_length:
                continue
            is_present = False
            for pos in range(w_length - s_length + 1):
                if word[pos:pos + s_length] == substr:
                    is_present = True
                    break
            if is_present:
                result += 1
        return result
