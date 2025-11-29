class C1(object):

    def minimumFlips(self, a1, a2):
        v1 = float('inf')

        def evaluate(a1):
            if a1.left is None and a1.right is None:
                v1 = a1.val
                return (v1, 1 - v1)
            if a1.val == 5:
                v2 = a1.left or a1.right
                v3, v4 = evaluate(v2)
                return (v4, v3)
            v5, v6 = evaluate(a1.left)
            v7, v8 = evaluate(a1.right)
            if a1.val == 2:
                v9 = v5 + v7
                v10 = min(v5 + v8, v6 + v7, v6 + v8)
            elif a1.val == 3:
                v9 = min(v5 + v7, v5 + v8, v6 + v7)
                v10 = v6 + v8
            elif a1.val == 4:
                v9 = min(v5 + v7, v6 + v8)
                v10 = min(v5 + v8, v6 + v7)
            else:
                v9 = v10 = v1
            return (v9, v10)
        v2, v3 = evaluate(a1)
        return v2 if not a2 else v3
