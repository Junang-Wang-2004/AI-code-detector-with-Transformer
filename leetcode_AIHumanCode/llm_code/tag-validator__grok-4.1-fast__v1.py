class Solution:
    def isValid(self, code):
        n = len(code)
        stk = []

        def get_tag(pos):
            if pos >= n or code[pos] != '<':
                return None, pos
            end = code.find('>', pos + 1)
            if end == -1 or end - pos - 1 < 1 or end - pos - 1 > 9:
                return None, pos
            nm = code[pos + 1:end]
            if not all('A' <= c <= 'Z' for c in nm):
                return None, pos
            return nm, end + 1

        def chk_close(pos, tg):
            ln = len(tg)
            fin = pos + ln + 3
            if fin > n or code[pos:pos + 2] != '</' or code[pos + 2:pos + 2 + ln] != tg or code[pos + 2 + ln] != '>':
                return False, pos
            return True, fin

        pos = 0
        tag, pos = get_tag(pos)
        if tag is None:
            return False
        stk.append(tag)

        while pos < n:
            if code[pos] == '<':
                if pos + 9 <= n and code[pos:pos + 9] == '<![CDATA[':
                    end = code.find(']]>', pos + 9)
                    if end == -1:
                        return False
                    pos = end + 3
                    continue
                if pos + 1 < n and code[pos + 1] == '/':
                    success, new_pos = chk_close(pos, stk[-1])
                    if not success:
                        return False
                    pos = new_pos
                    stk.pop()
                    if not stk:
                        return pos == n
                else:
                    tag, new_pos = get_tag(pos)
                    if tag is None:
                        return False
                    pos = new_pos
                    stk.append(tag)
            else:
                nxt = code.find('<', pos)
                pos = n if nxt == -1 else nxt

        return False
