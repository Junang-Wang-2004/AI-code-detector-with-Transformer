import collections

class C1(object):

    def findClosestLeaf(self, a1, a2):
        """
        """

        def traverse(a1, a2, a3):
            if not a1:
                return
            if not a1.left and (not a1.right):
                a3.add(a1.val)
                return
            if a1.left:
                a2[a1.val].append(a1.left.val)
                a2[a1.left.val].append(a1.val)
                traverse(a1.left, a2, a3)
            if a1.right:
                a2[a1.val].append(a1.right.val)
                a2[a1.right.val].append(a1.val)
                traverse(a1.right, a2, a3)
        v1, v2 = (collections.defaultdict(list), set())
        traverse(a1, v1, v2)
        v3, v4 = ([a2], set([a2]))
        while v3:
            v5 = []
            for v6 in v3:
                if v6 in v2:
                    return v6
                for v7 in v1[v6]:
                    if v7 in v4:
                        continue
                    v4.add(v7)
                    v5.append(v7)
            v3 = v5
        return 0
