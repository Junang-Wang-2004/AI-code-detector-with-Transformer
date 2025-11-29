class C1(object):
    v1 = 0
    v2 = 1
    v3 = 2
    v4 = 3
    v5 = 4
    v6 = 5

class C2(object):

    def isNumber(self, a1):
        """
        """
        import re
        return bool(re.match('^\\s*[\\+-]?((\\d+(\\.\\d*)?)|\\.\\d+)([eE][\\+-]?\\d+)?\\s*$', a1))
