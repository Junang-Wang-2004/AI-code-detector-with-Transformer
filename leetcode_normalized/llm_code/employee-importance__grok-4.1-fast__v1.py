class C1(object):

    def getImportance(self, a1, a2):
        v1 = {e.id: e.importance for v2 in a1}
        v3 = {v2.id: v2.subordinates for v2 in a1}

        def calc(a1):
            return v1.get(a1, 0) + sum((calc(c) for v1 in v3.get(a1, [])))
        return calc(a2)
