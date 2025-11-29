class C1:

    def sumOfEncryptedInt(self, a1):

        def encrypt(a1):
            v1 = str(a1)
            v2 = max((int(d) for v3 in v1))
            v4 = '1' * len(v1)
            return v2 * int(v4)
        v1 = 0
        for v2 in a1:
            v1 += encrypt(v2)
        return v1
