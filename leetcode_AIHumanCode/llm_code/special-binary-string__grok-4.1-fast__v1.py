class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        def process(segment: str) -> str:
            subs = []
            idx = 0
            slen = len(segment)
            while idx < slen:
                lvl = 0
                st = idx
                while idx < slen:
                    lvl += 1 if segment[idx] == '1' else -1
                    idx += 1
                    if lvl == 0:
                        break
                inside = process(segment[st + 1: idx - 1])
                subs.append('1' + inside + '0')
            subs.sort(reverse=True)
            return ''.join(subs)
        return process(S)
