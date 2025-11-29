class C1(object):

    def decodeString(self, a1):
        """
        """
        v1, v2, v3, v4 = (0, [], [], [])
        for v5 in a1:
            if v5.isdigit():
                v1 = v1 * 10 + ord(v5) - ord('0')
            elif v5.isalpha():
                v2.append(v5)
            elif v5 == '[':
                v3.append(v1)
                v4.append(v2)
                v1, v2 = (0, [])
            elif v5 == ']':
                v4[-1].extend(v2 * v3.pop())
                v2 = v4.pop()
        return ''.join(v2)
