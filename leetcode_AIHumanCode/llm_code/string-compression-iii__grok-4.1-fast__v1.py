class Solution(object):
    def compressedString(self, word):
        output = []
        pos = 0
        length = len(word)
        while pos < length:
            start = pos
            while pos < length and word[pos] == word[start]:
                pos += 1
            run_len = pos - start
            while run_len > 0:
                chunk = min(9, run_len)
                output.append(str(chunk) + word[start])
                run_len -= chunk
        return "".join(output)
