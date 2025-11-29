# Time:  O(n)
# Space: O(1)

class InputType(object):
    INVALID    = 0
    SPACE      = 1
    SIGN       = 2
    DIGIT      = 3
    DOT        = 4
    EXPONENT   = 5


# regular expression: "^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$"
# automata: http://images.cnitblog.com/i/627993/201405/012016243309923.png
class Solution2(object):
    def isNumber(self, s):
        """
        """
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))


