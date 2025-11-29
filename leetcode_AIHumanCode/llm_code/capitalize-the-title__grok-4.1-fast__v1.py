class Solution(object):
    def capitalizeTitle(self, title):
        chars = list(title.lower())
        n = len(chars)
        i = 0
        while i < n:
            if chars[i] == ' ':
                i += 1
                continue
            start = i
            while i < n and chars[i] != ' ':
                i += 1
            if i - start > 2:
                chars[start] = chars[start].upper()
        return "".join(chars)
