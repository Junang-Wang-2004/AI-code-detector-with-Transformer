class C1(object):

    def kMirror(self, a1, a2):
        """
        """

        def mirror(a1, a2, a3):
            v1 = a1
            if a3:
                a1 //= a2
            while a1:
                v1 = v1 * a2 + a1 % a2
                a1 //= a2
            return v1

        def num_gen(a1):
            v1, v2 = ([1] * 2, [a1] * 2)
            v3 = 1
            while True:
                v4 = mirror(v1[v3], a1, v3)
                v1[v3] += 1
                if v1[v3] == v2[v3]:
                    v2[v3] *= a1
                    v3 ^= 1
                yield v4

        def reverse(a1, a2):
            v1 = 0
            while a1:
                v1 = v1 * a2 + a1 % a2
                a1 = a1 // a2
            return v1

        def mirror_num(a1, a2):
            while True:
                v1 = next(a1)
                if v1 == reverse(v1, a2):
                    break
            return v1
        v1, v2 = (a1, 10)
        v3 = num_gen(v1)
        return sum((mirror_num(v3, v2) for v4 in range(a2)))
