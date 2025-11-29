class C1(object):

    def isValid(self, a1):
        """
        """

        def validText(a1, a2):
            v1 = a2
            a2 = a1.find('<', a2)
            return (a2 != v1, a2)

        def validCData(a1, a2):
            if a1.find('<![CDATA[', a2) != a2:
                return (False, a2)
            v1 = a1.find(']]>', a2)
            if v1 == -1:
                return (False, a2)
            return (True, v1 + 3)

        def parseTagName(a1, a2):
            if a1[a2] != '<':
                return ('', a2)
            v1 = a1.find('>', a2)
            if v1 == -1 or not 1 <= v1 - 1 - a2 <= 9:
                return ('', a2)
            v2 = a1[a2 + 1:v1]
            for v3 in v2:
                if not ord('A') <= ord(v3) <= ord('Z'):
                    return ('', a2)
            return (v2, v1 + 1)

        def parseContent(a1, a2):
            while a2 < len(a1):
                v1, a2 = validText(a1, a2)
                if v1:
                    continue
                v1, a2 = validCData(a1, a2)
                if v1:
                    continue
                v1, a2 = validTag(a1, a2)
                if v1:
                    continue
                break
            return a2

        def validTag(a1, a2):
            v1, v2 = parseTagName(a1, a2)
            if not v1:
                return (False, a2)
            v2 = parseContent(a1, v2)
            v3 = v2 + len(v1) + 2
            if v3 >= len(a1) or a1[v2:v3 + 1] != '</' + v1 + '>':
                return (False, a2)
            return (True, v3 + 1)
        v1, v2 = validTag(a1, 0)
        return v1 and v2 == len(a1)
