# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def entityParser(self, text):
        """
        """
        patterns = ["&quot;", "&apos;", "&amp;", "&gt;", "&lt;", "&frasl;"]
        chars = ["\"", "'", "&", ">", "<", "/"]
        result = []
        i, j = 0, 0
        while i != len(text):
            if text[i] != '&':                    
                result.append(text[i])
                i += 1
            else:
                for j, pattern in enumerate(patterns):
                    if pattern == text[i:i+len(pattern)]:
                        result.append(chars[j])
                        i += len(pattern)
                        break
                else:
                    result.append(text[i])
                    i += 1
        return "".join(result)
