class C1(object):

    def generateAbbreviations(self, a1):
        """
        """

        def generateAbbreviationsHelper(a1, a2, a3, a4):
            if a2 == len(a1):
                a4.append(''.join(a3))
                return
            a3.append(a1[a2])
            generateAbbreviationsHelper(a1, a2 + 1, a3, a4)
            a3.pop()
            if not a3 or not a3[-1][-1].isdigit():
                for v1 in range(1, len(a1) - a2 + 1):
                    a3.append(str(v1))
                    generateAbbreviationsHelper(a1, a2 + v1, a3, a4)
                    a3.pop()
        v1, v2 = ([], [])
        generateAbbreviationsHelper(a1, 0, v2, v1)
        return v1
