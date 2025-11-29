class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        idx = 0
        num_words = len(words)
        while idx < num_words:
            end = idx + 1
            curr_width = len(words[idx])
            while (end < num_words and
                   curr_width + len(words[end]) + 1 <= maxWidth):
                curr_width += len(words[end]) + 1
                end += 1
            count = end - idx
            total_len = sum(len(w) for w in words[idx:end])
            if count == 1 or end == num_words:
                justified = ' '.join(words[idx:end])
                justified += ' ' * (maxWidth - len(justified))
            else:
                extra_spaces = maxWidth - total_len
                per_gap = extra_spaces // (count - 1)
                remain = extra_spaces % (count - 1)
                line_parts = []
                for k in range(count):
                    line_parts.append(words[idx + k])
                    if k < count - 1:
                        gap_size = per_gap + (1 if k < remain else 0)
                        line_parts.append(' ' * gap_size)
                justified = ''.join(line_parts)
            result.append(justified)
            idx = end
        return result
