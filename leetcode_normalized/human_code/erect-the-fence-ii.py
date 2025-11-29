import random

class C1(object):

    def outerTrees(self, a1):
        """
        """

        def dist(a1, a2):
            return ((a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2) ** 0.5

        def inside(a1, a2):
            return dist(a1[0], a2) < a1[1] + EPS

        def circle_center(a1, a2, a3, a4):
            v1 = a1 * a1 + a2 * a2
            v2 = a3 * a3 + a4 * a4
            v3 = a1 * a4 - a2 * a3
            return [float(a4 * v1 - a2 * v2) / (2 * v3), float(a1 * v2 - a3 * v1) / (2 * v3)]

        def circle_from_2_points(a1, a2):
            v1 = [(a1[0] + a2[0]) / 2.0, (a1[1] + a2[1]) / 2.0]
            return [v1, dist(a1, a2) / 2.0]

        def circle_from_3_points(a1, a2, a3):
            v1 = circle_center(a2[0] - a1[0], a2[1] - a1[1], a3[0] - a1[0], a3[1] - a1[1])
            v1[0] += a1[0]
            v1[1] += a1[1]
            return [v1, dist(v1, a1)]

        def trivial(a1):
            if not a1:
                return None
            if len(a1) == 1:
                return [a1[0], 0.0]
            if len(a1) == 2:
                return circle_from_2_points(a1[0], a1[1])
            return circle_from_3_points(a1[0], a1[1], a1[2])

        def Welzl(a1, a2, a3):
            if a3 == len(a1) or len(a2) == 3:
                return trivial(a2)
            v1 = Welzl(a1, a2, a3 + 1)
            if v1 is not None and inside(v1, a1[a3]):
                return v1
            a2.append(a1[a3])
            v1 = Welzl(a1, a2, a3 + 1)
            a2.pop()
            return v1
        v1 = 1e-05
        random.seed(0)
        random.shuffle(a1)
        v2 = Welzl(a1, [], 0)
        return (v2[0][0], v2[0][1], v2[1])
