class C1(object):

    def removeNodes(self, a1):

        def process(a1):
            if not a1:
                return (None, float('-inf'))
            v1, v2 = process(a1.next)
            if a1.val > v2:
                a1.next = v1
                return (a1, a1.val)
            return (v1, v2)
        v1, v2 = process(a1)
        return v1
