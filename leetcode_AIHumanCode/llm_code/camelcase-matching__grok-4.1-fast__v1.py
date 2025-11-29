class Solution(object):
    def camelMatch(self, queries, pattern):
        def check_match(text, template):
            idx = 0
            tlen = len(template)
            for sym in text:
                advanced = False
                if idx < tlen and sym == template[idx]:
                    idx += 1
                    advanced = True
                if sym.isupper() and not advanced:
                    return False
            return idx == tlen

        return [check_match(txt, pattern) for txt in queries]
