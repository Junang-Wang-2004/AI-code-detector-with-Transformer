class C1(object):

    def largestValues(self, a1):
        """
        """

        def largestValuesHelper(a1, a2, a3):
            if not a1:
                return
            if a2 == len(a3):
                a3.append(a1.val)
            else:
                a3[a2] = max(a3[a2], a1.val)
            largestValuesHelper(a1.left, a2 + 1, a3)
            largestValuesHelper(a1.right, a2 + 1, a3)
        v1 = []
        largestValuesHelper(a1, 0, v1)
        return v1
