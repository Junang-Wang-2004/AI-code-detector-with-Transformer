class Solution:
    def ambiguousCoordinates(self, S):
        digits = S[1:-1]
        m = len(digits)
        output = []
        for sep in range(1, m):
            lsize = sep
            for p1 in range(1, lsize + 1):
                front1 = digits[:p1]
                back1 = digits[p1:sep]
                if len(front1) > 1 and front1[0] == '0':
                    continue
                if back1 and back1[-1] == '0':
                    continue
                x = front1 + ('.' + back1 if back1 else '')
                rstart = sep
                rsize = m - rstart
                for p2 in range(1, rsize + 1):
                    front2 = digits[rstart:rstart + p2]
                    back2 = digits[rstart + p2:]
                    if len(front2) > 1 and front2[0] == '0':
                        continue
                    if back2 and back2[-1] == '0':
                        continue
                    y = front2 + ('.' + back2 if back2 else '')
                    output.append("({}, {})".format(x, y))
        return output
