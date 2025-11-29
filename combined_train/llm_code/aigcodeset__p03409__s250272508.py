import sys
from io import StringIO
import unittest
v1 = []

def f1(a1, a2, a3):
    for next in v1[a1]:
        if str(next) in a2:
            continue
        a2.append(str(next))
        f1(next, a2, a3)
        if a3[next] == -1:
            if not a3[a1] == -1:
                a3[a3[a1]] = -1
                a3[a1] = -1
            a3[a1] = next
            a3[next] = a1
            return
    return

def f2():
    global graphs
    v1 = int(input())
    v2 = [[int(i) for v3 in input().split()] for v4 in range(v1)]
    v5 = [[int(v3) for v3 in input().split()] for v4 in range(v1)]
    v6 = [[] for v3 in range(v1 * 2)]
    for v3, v7 in enumerate(v2):
        for v4, v8 in enumerate(v5):
            if v7[0] < v8[0] and v7[1] < v8[1]:
                v6[v3].append(v1 + v4)
                v6[v1 + v4].append(v3)
    v9 = [-1 for v3 in range(v1 * 2)]
    v10 = []
    for v11 in range(v1 * 2):
        f1(v11, v10, v9)
    v12 = [not v3 == -1 for v3 in v9].count(True) // 2
    print(int(v12))

class C1(unittest.TestCase):

    def assertIO(self, a1, a2):
        v1, v2 = (sys.stdout, sys.stdin)
        sys.stdout, sys.stdin = (StringIO(), StringIO(a1))
        f2()
        sys.stdout.seek(0)
        v3 = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = (v1, v2)
        self.assertEqual(v3, a2)

    def test_入力例_1(self):
        input = '3\n2 0\n3 1\n1 3\n4 2\n0 4\n5 5'
        v1 = '2'
        self.assertIO(input, v1)

    def test_入力例_2(self):
        input = '3\n0 0\n1 1\n5 2\n2 3\n3 4\n4 5'
        v1 = '2'
        self.assertIO(input, v1)

    def test_入力例_3(self):
        input = '2\n2 2\n3 3\n0 0\n1 1'
        v1 = '0'
        self.assertIO(input, v1)

    def test_入力例_4(self):
        input = '5\n0 0\n7 3\n2 2\n4 8\n1 6\n8 5\n6 9\n5 4\n9 1\n3 7'
        v1 = '5'
        self.assertIO(input, v1)

    def test_入力例_5(self):
        input = '5\n0 0\n1 1\n5 5\n6 6\n7 7\n2 2\n3 3\n4 4\n8 8\n9 9'
        v1 = '4'
        self.assertIO(input, v1)
if __name__ == '__main__':
    f2()
