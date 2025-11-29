class Solution:
    def applySubstitutions(self, replacements, text):
        mapping = dict(replacements)
        cache = {}

        def substitute(content):
            if content in cache:
                return cache[content]
            parts = []
            pos = 0
            while pos < len(content):
                pct_start = content.find('%', pos)
                if pct_start == -1:
                    parts.append(content[pos:])
                    break
                if pct_start > pos:
                    parts.append(content[pos:pct_start])
                pos = pct_start
                pct_end = content.find('%', pos + 1)
                if pct_end == -1:
                    parts.append(content[pos:])
                    break
                key = content[pos + 1:pct_end]
                parts.append(substitute(mapping[key]))
                pos = pct_end + 1
            result = ''.join(parts)
            cache[content] = result
            return result

        return substitute(text)
