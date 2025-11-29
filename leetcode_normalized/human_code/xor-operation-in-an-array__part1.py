class C1(object):

    def xorOperation(self, a1, a2):
        """
        """

        def xorNums(a1, a2):

            def xorNumsBeginEven(a1, a2):
                assert a2 % 2 == 0
                return a1 // 2 % 2 ^ (a2 + a1 - 1 if a1 % 2 else 0)
            return a2 ^ xorNumsBeginEven(a1 - 1, a2 + 1) if a2 % 2 else xorNumsBeginEven(a1, a2)
        return int(a1 % 2 and a2 % 2) + 2 * xorNums(a1, a2 // 2)
