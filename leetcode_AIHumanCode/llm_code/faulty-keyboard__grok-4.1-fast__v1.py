import collections

class Solution:
    def finalString(self, s):
        buffer = collections.deque()
        rev = False
        for ch in s:
            if ch != 'i':
                if rev:
                    buffer.appendleft(ch)
                else:
                    buffer.append(ch)
            else:
                rev = not rev
        if rev:
            buffer.reverse()
        return ''.join(buffer)
