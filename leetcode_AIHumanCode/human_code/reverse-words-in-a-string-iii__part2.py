# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def reverseWords(self, s):
        reversed_words = [word[::-1] for word in s.split(' ')]
        return ' '.join(reversed_words)

