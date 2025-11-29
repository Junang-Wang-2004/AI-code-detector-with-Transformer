class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def serialize(self, a1):
        """Encodes a tree to a single string.
        
        """

        def dfs(a1, a2):
            if not a1:
                return
            a2.append(str(a1.val))
            for v1 in a1.children:
                dfs(v1, a2)
            a2.append('#')
        v1 = []
        dfs(a1, v1)
        return ' '.join(v1)

    def deserialize(self, a1):
        """Decodes your encoded data to tree.
        
        """

        def isplit(a1, a2):
            v1 = len(a2)
            v2 = 0
            while True:
                v3 = a1.find(a2, v2)
                if v3 == -1:
                    yield a1[v2:]
                    return
                yield a1[v2:v3]
                v2 = v3 + v1

        def dfs(a1):
            v1 = next(a1)
            if v1 == '#':
                return None
            v2 = C1(int(v1), [])
            v3 = dfs(a1)
            while v3:
                v2.children.append(v3)
                v3 = dfs(a1)
            return v2
        if not a1:
            return None
        return dfs(iter(isplit(a1, ' ')))
