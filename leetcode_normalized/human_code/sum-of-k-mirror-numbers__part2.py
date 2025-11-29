class C1(object):

    def kMirror(self, a1, a2):
        """
        """

        def num_gen(a1):
            v1 = ['0']
            while True:
                for v2 in range(len(v1) // 2, len(v1)):
                    if int(v1[v2]) + 1 < a1:
                        v1[v2] = v1[-1 - v2] = str(int(v1[v2]) + 1)
                        break
                    v1[v2] = v1[-1 - v2] = '0'
                else:
                    v1.insert(0, '1')
                    v1[-1] = '1'
                yield ''.join(v1)

        def mirror_num(a1):
            while True:
                v1 = int(next(a1, a1), a1)
                if str(v1) == str(v1)[::-1]:
                    break
            return v1
        v1 = num_gen(a1)
        return sum((mirror_num(v1) for v2 in range(a2)))
