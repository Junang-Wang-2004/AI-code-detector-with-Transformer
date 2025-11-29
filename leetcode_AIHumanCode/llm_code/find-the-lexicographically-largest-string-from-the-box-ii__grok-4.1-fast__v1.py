class Solution:
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word
        n = len(word)
        best_start = 0
        match_length = 0
        cursor = 1
        while cursor < n:
            if word[cursor] == word[best_start + match_length]:
                match_length += 1
                cursor += 1
            elif word[cursor] < word[best_start + match_length]:
                match_length = 0
                cursor += 1
            else:
                back_pos = cursor - match_length
                if word[back_pos] >= word[cursor]:
                    best_start = back_pos
                else:
                    best_start = cursor
                match_length = 0
                cursor += 1
        skip_end = max(numFriends - 1 - best_start, 0)
        return word[best_start:n - skip_end]
