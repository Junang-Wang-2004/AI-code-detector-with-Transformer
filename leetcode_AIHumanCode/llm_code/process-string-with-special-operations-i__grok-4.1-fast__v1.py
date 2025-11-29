class Solution(object):
    def processStr(self, s):
        buffer = []
        for ch in s:
            if ch == '*':
                if buffer:
                    buffer.pop()
            elif ch == '#':
                buffer.extend(buffer)
            elif ch == '%':
                buffer.reverse()
            else:
                buffer.append(ch)
        return ''.join(buffer)
