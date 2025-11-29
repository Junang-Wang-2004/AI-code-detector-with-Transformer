class Solution(object):
    def boldWords(self, words, S):
        matches = []
        length = len(S)
        for start_pos in range(length):
            for substring in words:
                sub_len = len(substring)
                if start_pos + sub_len > length:
                    continue
                if S[start_pos:start_pos + sub_len] == substring:
                    matches.append((start_pos, start_pos + sub_len - 1))
        if not matches:
            return S
        matches.sort()
        combined = [list(matches[0])]
        for c_start, c_end in matches[1:]:
            p_start, p_end = combined[-1]
            if p_end + 1 >= c_start:
                combined[-1][1] = max(p_end, c_end)
            else:
                combined.append([c_start, c_end])
        parts = []
        cursor = 0
        for b_start, b_end in combined:
            parts.append(S[cursor:b_start])
            parts.append("<b>")
            parts.append(S[b_start:b_end + 1])
            parts.append("</b>")
            cursor = b_end + 1
        parts.append(S[cursor:])
        return "".join(parts)
