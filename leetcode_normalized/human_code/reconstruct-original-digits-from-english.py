from collections import Counter

class C1(object):

    def originalDigits(self, a1):
        """
        """
        v1 = [Counter(_) for v2 in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]
        v3 = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        v4 = ['z', 'o', 'w', 't', 'u', 'f', 'x', 's', 'g', 'n']
        v5 = Counter(list(a1))
        v6 = []
        for v7 in v3:
            while v5[v4[v7]] > 0:
                v5 -= v1[v7]
                v6.append(v7)
        v6.sort()
        return ''.join(map(str, v6))
