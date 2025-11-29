class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def serialize(self, a1):
        """Encodes a tree to a single string.

        """

        def serializeHelper(a1):
            if not a1:
                vals.append('#')
                return
            vals.append(str(a1.val))
            serializeHelper(a1.left)
            serializeHelper(a1.right)
        v1 = []
        serializeHelper(a1)
        return ' '.join(v1)

    def deserialize(self, a1):
        """Decodes your encoded data to tree.

        """

        def deserializeHelper():
            v1 = next(vals)
            if v1 == '#':
                return None
            v2 = C1(int(v1))
            v2.left = deserializeHelper()
            v2.right = deserializeHelper()
            return v2

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
        v1 = iter(isplit(a1, ' '))
        return deserializeHelper()

class C3(object):

    def serialize(self, a1):
        """Encodes a tree to a single string.
        
        """

        def gen_preorder(a1):
            if not a1:
                yield '#'
            else:
                yield str(a1.val)
                for v1 in gen_preorder(a1.left):
                    yield v1
                for v1 in gen_preorder(a1.right):
                    yield v1
        return ' '.join(gen_preorder(a1))

    def deserialize(self, a1):
        """Decodes your encoded data to tree.
        
        """

        def builder(a1):
            v1 = next(a1)
            if v1 == '#':
                return None
            v2 = C1(int(v1))
            v2.left = builder(a1)
            v2.right = builder(a1)
            return v2
        v1 = iter(a1.split())
        return builder(v1)
