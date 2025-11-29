class C1:

    def discountPrices(self, a1: str, a2: int) -> str:
        v1 = a1.split()
        v2 = []
        for v3 in v1:
            if v3 and v3[0] == '$' and v3[1:].isdigit():
                v4 = int(v3[1:])
                v5 = v4 * (100 - a2)
                v6 = v5 // 100
                v7 = v5 % 100
                v2.append(f'${v6}.{v7:02d}')
            else:
                v2.append(v3)
        return ' '.join(v2)
