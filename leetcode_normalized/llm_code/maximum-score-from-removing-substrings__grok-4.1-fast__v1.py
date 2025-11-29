class C1(object):

    def maximumGain(self, a1, a2, a3):

        def eliminate(a1, a2, a3, a4):
            v1 = 0
            v2 = []
            for v3 in a1:
                v2.append(v3)
                while len(v2) >= 2 and v2[-2] == a2 and (v2[-1] == a3):
                    v2.pop()
                    v2.pop()
                    v1 += a4
            return (v1, ''.join(v2))
        if a2 >= a3:
            v1, v2 = eliminate(a1, 'a', 'b', a2)
            v3, v4 = eliminate(v2, 'b', 'a', a3)
            return v1 + v3
        else:
            v1, v2 = eliminate(a1, 'b', 'a', a3)
            v3, v4 = eliminate(v2, 'a', 'b', a2)
            return v1 + v3
