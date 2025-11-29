class Solution(object):
    def hasMatch(self, s, p):
        segments = [part for part in p.split('*') if part]
        curr = 0
        for part in segments:
            found = s.find(part, curr)
            if found == -1:
                return False
            curr = found + len(part)
        return True
