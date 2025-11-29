# Time:  O(r * 2^r)
# Space: O(r * 2^r)
# memoization
class Solution2(object):
    def applySubstitutions(self, replacements, text):
        """
        """
        lookup = {k:v for k, v in replacements}
        memo = {}
        def replace(s):
            if s not in memo:
                result = []
                i = 0
                while i < len(s):
                    if s[i] != '%':
                        result.append(s[i])
                        i += 1
                        continue
                    j = next(j for j in range(i+1, len(s)) if s[j] == '%')
                    result.append(replace(lookup[s[i+1:j]]))
                    i = j+1
                memo[s] = "".join(result)
            return memo[s]

        return replace(text)
