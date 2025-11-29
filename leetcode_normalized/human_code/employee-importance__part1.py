import collections
"\n# Employee info\nclass Employee(object):\n    def __init__(self, id, importance, subordinates):\n        # It's the unique id of each node.\n        # unique id of this employee\n        self.id = id\n        # the importance value of this employee\n        self.importance = importance\n        # the id of direct subordinates\n        self.subordinates = subordinates\n"

class C1(object):

    def getImportance(self, a1, a2):
        """
        """
        if a1[a2 - 1] is None:
            return 0
        v1 = a1[a2 - 1].importance
        for a2 in a1[a2 - 1].subordinates:
            v1 += self.getImportance(a1, a2)
        return v1
