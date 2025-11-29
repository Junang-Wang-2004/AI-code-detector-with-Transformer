class Solution:
    def countValidWords(self, sentence):
        def is_valid(word):
            if not word:
                return False
            n = len(word)
            saw_hyphen = False
            for pos in range(n):
                ch = word[pos]
                if ch.isdigit():
                    return False
                if ch == '-':
                    if saw_hyphen or pos == 0 or pos == n - 1 or not (word[pos - 1].isalpha() and word[pos + 1].isalpha()):
                        return False
                    saw_hyphen = True
                elif ch in '!,.':
                    if pos != n - 1:
                        return False
                elif not ch.isalpha():
                    return False
            return True
        return sum(1 for w in sentence.split() if is_valid(w))
