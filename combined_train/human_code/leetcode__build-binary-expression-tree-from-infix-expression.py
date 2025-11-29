class C1(object):

    def __init__(self, a1=' ', a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def expTree(self, a1):
        """
        """

        def compute(a1, a2):
            v1, v2 = (a1.pop(), a1.pop())
            a1.append(C1(val=a2.pop(), left=v2, right=v1))
        v1 = {'+': 0, '-': 0, '*': 1, '/': 1}
        v2, v3, v4 = ([], [], 0)
        for v5 in range(len(a1)):
            if a1[v5].isdigit():
                v4 = v4 * 10 + int(a1[v5])
                if v5 == len(a1) - 1 or not a1[v5 + 1].isdigit():
                    v2.append(C1(val=str(v4)))
                    v4 = 0
            elif a1[v5] == '(':
                v3.append(a1[v5])
            elif a1[v5] == ')':
                while v3[-1] != '(':
                    compute(v2, v3)
                v3.pop()
            elif a1[v5] in v1:
                while v3 and v3[-1] in v1 and (v1[v3[-1]] >= v1[a1[v5]]):
                    compute(v2, v3)
                v3.append(a1[v5])
        while v3:
            compute(v2, v3)
        return v2[-1]
