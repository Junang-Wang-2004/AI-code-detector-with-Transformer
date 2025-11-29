class Solution(object):
    def strWithout3a3b(self, A, B):
        res = []
        ca, cb = A, B
        last_ch = None
        cnt = 0
        while ca or cb:
            use_a = (cnt < 2 and ca >= cb) or (cnt == 2 and last_ch == 'b')
            if use_a and ca > 0:
                res.append('a')
                ca -= 1
                if last_ch == 'a':
                    cnt += 1
                else:
                    cnt = 1
                    last_ch = 'a'
            else:
                res.append('b')
                cb -= 1
                if last_ch == 'b':
                    cnt += 1
                else:
                    cnt = 1
                    last_ch = 'b'
        return "".join(res)
