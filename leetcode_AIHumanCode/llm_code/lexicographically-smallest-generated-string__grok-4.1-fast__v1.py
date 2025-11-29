import collections

class Solution(object):
    def generateString(self, pat, txt):
        n, mm = len(txt), len(pat)
        zpat = self._zarray(pat)

        canvas = ['?'] * (n + mm - 1)
        prev_t = -mm
        for start in range(n):
            if txt[start] != 'T':
                continue
            sep = start - prev_t
            if sep < mm:
                if zpat[sep] < mm - sep:
                    return ''
                for off in range(sep):
                    canvas[start + (mm - sep) + off] = pat[(mm - sep) + off]
            else:
                for off in range(mm):
                    canvas[start + off] = pat[off]
            prev_t = start

        chg = []
        for idx in range(n + mm - 1):
            if canvas[idx] == '?':
                canvas[idx] = 'a'
                chg.append(idx)

        concat = pat + '$' + canvas
        zconc = self._zarray(concat)
        q = collections.deque()
        ptr = 0
        scan = mm + 1
        while scan < mm + 1 + n:
            pidx = scan - mm - 1
            while q and q[0] < scan:
                q.popleft()
            while ptr < len(chg) and (mm + 1 + chg[ptr]) <= scan + mm - 1:
                q.append(mm + 1 + chg[ptr])
                ptr += 1
            if txt[pidx] == 'F' and zconc[scan] == mm:
                if not q:
                    return ''
                tochg = q[-1]
                canvas[tochg - mm - 1] = 'b'
                scan += mm
            else:
                scan += 1
        return ''.join(canvas)

    def _zarray(self, seq):
        sz = len(seq)
        zar = [0] * sz
        lft = rgt = 0
        for i in range(1, sz):
            if i < rgt:
                zar[i] = min(rgt - i, zar[i - lft])
            while i + zar[i] < sz and seq[zar[i]] == seq[i + zar[i]]:
                zar[i] += 1
            if i + zar[i] > rgt:
                lft = i
                rgt = i + zar[i]
        return zar
