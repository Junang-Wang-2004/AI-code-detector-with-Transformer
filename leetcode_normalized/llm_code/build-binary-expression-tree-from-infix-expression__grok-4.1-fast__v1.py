class C1(object):

    def __init__(self, a1=' ', a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def expTree(self, a1):
        v1 = {'+': 0, '-': 0, '*': 1, '/': 1}
        v2 = []
        v3 = []
        v4 = 0
        while v4 < len(a1):
            v5 = a1[v4]
            if v5.isdigit():
                v6 = 0
                while v4 < len(a1) and a1[v4].isdigit():
                    v6 = v6 * 10 + int(a1[v4])
                    v4 += 1
                v2.append(str(v6))
                continue
            if v5 == '(':
                v3.append(v5)
            elif v5 == ')':
                while v3 and v3[-1] != '(':
                    v2.append(v3.pop())
                v3.pop()
            elif v5 in v1:
                while v3 and v3[-1] != '(' and (v1[v3[-1]] >= v1[v5]):
                    v2.append(v3.pop())
                v3.append(v5)
            v4 += 1
        while v3:
            v2.append(v3.pop())
        v7 = []
        for v8 in v2:
            if v8.isdigit():
                v7.append(C1(v8))
            else:
                v9 = v7.pop()
                v10 = v7.pop()
                v7.append(C1(v8, left=v10, right=v9))
        return v7[0]
