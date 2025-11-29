import collections
import functools

class C1(object):

    def checkEquivalence(self, a1, a2):
        """
        """

        def add_counter(a1, a2, a3, a4):
            if a4.isalpha():
                a1[ord(a4) - ord('a')] += a3 if a2[0] == '+' else -a3
            a2[0] = a4

        def inorder_traversal(a1, a2):

            def traverseLeft(a1, a2):
                while a1:
                    a2.append(a1)
                    a1 = a1.left
            v1 = []
            traverseLeft(a1, v1)
            while v1:
                v2 = v1.pop()
                a2(v2.val)
                traverseLeft(v2.right, v1)
        v1 = collections.defaultdict(int)
        inorder_traversal(a1, functools.partial(add_counter, v1, ['+'], 1))
        inorder_traversal(a2, functools.partial(add_counter, v1, ['+'], -1))
        return all((v == 0 for v2 in v1.values()))
