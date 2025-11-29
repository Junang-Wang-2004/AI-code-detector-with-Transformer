class C1(object):

    def toLowerCase(self, a1):
        """
        """
        return ''.join([chr(ord('a') + ord(c) - ord('A')) if 'A' <= c <= 'Z' else c for v1 in a1])
