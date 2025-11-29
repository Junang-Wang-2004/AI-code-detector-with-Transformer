import collections

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def serialize(self, a1):
        """Encodes a tree to a single string.

        """

        def serializeHelper(a1, a2):
            if a1:
                a2.append(a1.val)
                serializeHelper(a1.left, a2)
                serializeHelper(a1.right, a2)
        v1 = []
        serializeHelper(a1, v1)
        return ' '.join(map(str, v1))

    def deserialize(self, a1):
        """Decodes your encoded data to tree.

        """

        def deserializeHelper(a1, a2, a3):
            if not a3:
                return None
            if a1 < a3[0] < a2:
                v1 = a3.popleft()
                v2 = C1(v1)
                v2.left = deserializeHelper(a1, v1, a3)
                v2.right = deserializeHelper(v1, a2, a3)
                return v2
            else:
                return None
        v1 = collections.deque([int(val) for v2 in a1.split()])
        return deserializeHelper(float('-inf'), float('inf'), v1)
