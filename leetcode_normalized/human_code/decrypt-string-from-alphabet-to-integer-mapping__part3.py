import re

class C1(object):

    def freqAlphabets(self, a1):
        """
        """

        def alpha(a1):
            return chr(ord('a') + int(a1) - 1)
        return ''.join((alpha(i[:2]) for v1 in re.findall('\\d\\d#|\\d', a1)))
