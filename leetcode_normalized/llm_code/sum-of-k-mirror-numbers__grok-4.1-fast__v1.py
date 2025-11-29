class C1:

    def kMirror(self, a1, a2):

        def generate_pal_base_k(a1):
            v1 = [1]
            while True:
                yield v1[:]
                v2 = len(v1)
                v3 = v2 // 2
                while v3 < v2:
                    if v1[v3] < a1 - 1:
                        v1[v3] += 1
                        v1[v2 - 1 - v3] = v1[v3]
                        break
                    v1[v3] = 0
                    v1[v2 - 1 - v3] = 0
                    v3 += 1
                else:
                    v1.insert(0, 1)
                    v1[-1] = 1

        def decimal_value(a1, a2):
            v1 = 0
            for v2 in a1:
                v1 = v1 * a2 + v2
            return v1

        def is_decimal_palindrome(a1):
            v1 = 0
            v2 = a1
            while v2 > 0:
                v1 = v1 * 10 + v2 % 10
                v2 //= 10
            return v1 == a1
        v1 = generate_pal_base_k(a1)
        v2 = 0
        v3 = 0
        while v3 < a2:
            v4 = next(v1)
            v5 = decimal_value(v4, a1)
            if is_decimal_palindrome(v5):
                v2 += v5
                v3 += 1
        return v2
