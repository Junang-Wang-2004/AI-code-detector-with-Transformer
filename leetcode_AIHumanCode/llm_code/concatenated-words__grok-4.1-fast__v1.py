class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        dict_set = set(words)
        found_words = []
        for current_word in words:
            no_self = dict_set - {current_word}
            w_length = len(current_word)
            can_reach = [False] * (w_length + 1)
            can_reach[0] = True
            for pos in range(1, w_length + 1):
                for piece_size in range(1, pos + 1):
                    prev_pos = pos - piece_size
                    if can_reach[prev_pos] and current_word[prev_pos:pos] in no_self:
                        can_reach[pos] = True
                        break
            if can_reach[w_length]:
                found_words.append(current_word)
        return found_words
