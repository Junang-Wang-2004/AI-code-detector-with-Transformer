class C1(object):

    def minOperationsToFlip(self, a1):

        def parse_primary(a1):
            if a1[a1].isdigit():
                v1 = a1[a1]
                v2 = int(v1 != '0')
                v3 = int(v1 != '1')
                return ([v2, v3], a1 + 1)
            a1 += 1
            v5, a1 = parse_expression(a1)
            a1 += 1
            return (v5, a1)

        def parse_expression(a1):
            v1, a1 = parse_primary(a1)
            while a1 < len(a1) and a1[a1] in '&|':
                v3 = a1[a1]
                a1 += 1
                v4, a1 = parse_primary(a1)
                v5, v6 = v1
                v7, v8 = v4
                if v3 == '&':
                    v9 = min(v5, v7)
                    v10 = min(v6 + v8, 1 + min(v6, v8))
                else:
                    v9 = min(v5 + v7, 1 + min(v5, v7))
                    v10 = min(v6, v8)
                v1 = [v9, v10]
            return (v1, a1)
        v1, v2 = parse_expression(0)
        return max(v1)
