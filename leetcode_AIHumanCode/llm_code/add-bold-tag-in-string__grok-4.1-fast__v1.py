class Solution:
    def addBoldTag(self, s, words):
        matches = []
        for word in words:
            wlen = len(word)
            if wlen == 0:
                continue
            pos = 0
            while True:
                idx = s.find(word, pos)
                if idx == -1:
                    break
                matches.append((idx, idx + wlen))
                pos = idx + 1
        
        if not matches:
            return s
        
        matches.sort()
        bold_ranges = [[matches[0][0], matches[0][1]]]
        for start, end in matches[1:]:
            if start <= bold_ranges[-1][1]:
                bold_ranges[-1][1] = max(bold_ranges[-1][1], end)
            else:
                bold_ranges.append([start, end])
        
        parts = []
        cur = 0
        for begin, finish in bold_ranges:
            parts.append(s[cur:begin])
            parts.append("<b>")
            parts.append(s[begin:finish])
            parts.append("</b>")
            cur = finish
        parts.append(s[cur:])
        return "".join(parts)
