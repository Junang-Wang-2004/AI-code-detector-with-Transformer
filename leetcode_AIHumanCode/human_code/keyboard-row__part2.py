# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def findWords(self, words):
        """
        """
        keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        single_row_words = []
        for word in words:
            for row in keyboard_rows:
                if all(letter in row for letter in word.lower()):
                    single_row_words.append(word)
        return single_row_words

