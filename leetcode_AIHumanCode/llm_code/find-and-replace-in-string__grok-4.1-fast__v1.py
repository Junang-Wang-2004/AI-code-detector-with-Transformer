class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        replacements = {}
        for pos, src, tgt in zip(indexes, sources, targets):
            if S[pos:pos + len(src)] == src:
                replacements[pos] = (len(src), tgt)
        output = []
        pos = 0
        while pos < len(S):
            if pos in replacements:
                length, replacement = replacements[pos]
                output.append(replacement)
                pos += length
            else:
                output.append(S[pos])
                pos += 1
        return "".join(output)
