class C1(object):

    def __init__(self, a1=None):
        """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

    def isInteger(self):
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

    def add(self, a1):
        """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       """

    def setInteger(self, a1):
        """
       Set this NestedInteger to hold a single integer equal to value.
       """

    def getInteger(self):
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class C2(object):

    def deserialize(self, a1):
        if not a1:
            return C1()
        if a1[0] != '[':
            return C1(int(a1))
        v1 = []
        v2 = 0
        for v3 in range(len(a1)):
            if a1[v3] == '[':
                v1 += (C1(),)
                v2 = v3 + 1
            elif a1[v3] in ',]':
                if a1[v3 - 1].isdigit():
                    v1[-1].add(C1(int(a1[v2:v3])))
                if a1[v3] == ']' and len(v1) > 1:
                    v4 = v1[-1]
                    v1.pop()
                    v1[-1].add(v4)
                v2 = v3 + 1
        return v1[-1]
