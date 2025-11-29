class C1(object):

    def concatHex36(self, a1):
        """
        """
        v1 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        def convert(a1, a2):
            v1 = []
            while a1:
                a1, v3 = divmod(a1, a2)
                v1.append(v1[v3])
            v1.reverse()
            return ''.join(v1)
        return convert(a1 ** 2, 16) + convert(a1 ** 3, 36)
