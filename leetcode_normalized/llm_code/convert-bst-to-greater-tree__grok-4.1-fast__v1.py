class C1:

    def convertBST(self, a1):
        v1 = 0
        v2 = []
        v3 = a1
        while v2 or v3:
            while v3:
                v2.append(v3)
                v3 = v3.right
            v3 = v2.pop()
            v3.val += v1
            v1 = v3.val
            v3 = v3.left
        return a1
