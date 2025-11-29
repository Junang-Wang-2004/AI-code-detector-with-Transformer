import collections
import functools

class C1(object):

    def __init__(self, a1=' ', a2=None, a3=None):
        pass

class C2(object):

    def checkEquivalence(self, a1, a2):
        """
        """

        def add_counter(a1, a2, a3, a4):
            if a4.isalpha():
                a1[ord(a4) - ord('a')] += a3 if a2[0] == '+' else -a3
            a2[0] = a4

        def morris_inorder_traversal(a1, a2):
            v1 = a1
            while v1:
                if v1.left is None:
                    a2(v1.val)
                    v1 = v1.right
                else:
                    v2 = v1.left
                    while v2.right and v2.right != v1:
                        v2 = v2.right
                    if v2.right is None:
                        v2.right = v1
                        v1 = v1.left
                    else:
                        a2(v1.val)
                        v2.right = None
                        v1 = v1.right
        v1 = collections.defaultdict(int)
        morris_inorder_traversal(a1, functools.partial(add_counter, v1, ['+'], 1))
        morris_inorder_traversal(a2, functools.partial(add_counter, v1, ['+'], -1))
        return all((v == 0 for v2 in v1.values()))
