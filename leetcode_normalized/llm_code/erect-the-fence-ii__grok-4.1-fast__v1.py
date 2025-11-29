import random

class C1(object):

    def outerTrees(self, a1):

        def point_dist_sq(a1, a2, a3, a4):
            v1 = a1 - a3
            v2 = a2 - a4
            return v1 * v1 + v2 * v2

        def point_in_circle(a1, a2, a3, a4, a5):
            return point_dist_sq(a1, a2, a4, a5) <= a3 * a3 + 1e-09

        def make_circle_two(a1, a2):
            v1 = (a1[0] + a2[0]) / 2
            v2 = (a1[1] + a2[1]) / 2
            v3 = ((a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2) ** 0.5 / 2
            return (v1, v2, v3)

        def make_circle_three(a1, a2, a3):
            v1, v2 = a1
            v3, v4 = a2
            v5, v6 = a3
            v7 = v1 * (v4 - v6) + v3 * (v6 - v2) + v5 * (v2 - v4)
            v8 = 2 * v7
            if abs(v8) < 1e-09:
                v9 = point_dist_sq(v1, v2, v3, v4)
                v10 = point_dist_sq(v1, v2, v5, v6)
                v11 = point_dist_sq(v3, v4, v5, v6)
                if v9 >= v10 and v9 >= v11:
                    return make_circle_two(a1, a2)
                if v10 >= v9 and v10 >= v11:
                    return make_circle_two(a1, a3)
                return make_circle_two(a2, a3)
            v12 = v1 * v1 + v2 * v2
            v13 = v3 * v3 + v4 * v4
            v14 = v5 * v5 + v6 * v6
            v15 = (v12 * (v4 - v6) + v13 * (v6 - v2) + v14 * (v2 - v4)) / v8
            v16 = (v12 * (v5 - v3) + v13 * (v1 - v5) + v14 * (v3 - v1)) / v8
            v17 = ((v15 - v1) ** 2 + (v16 - v2) ** 2) ** 0.5
            return (v15, v16, v17)

        def trivial_case(a1):
            v1 = len(a1)
            if v1 == 0:
                return (0.0, 0.0, 0.0)
            if v1 == 1:
                return (a1[0][0], a1[0][1], 0.0)
            if v1 == 2:
                return make_circle_two(a1[0], a1[1])
            return make_circle_three(a1[0], a1[1], a1[2])

        def find_min_circle(a1, a2, a3):
            if a3 == len(a1) or len(a2) == 3:
                return trivial_case(a2)
            v1 = find_min_circle(a1, a2, a3 + 1)
            v2, v3 = a1[a3]
            if point_in_circle(*v1, v2, v3):
                return v1
            a2.append(a1[a3])
            v4 = find_min_circle(a1, a2, a3 + 1)
            a2.pop()
            return v4
        v1 = a1[:]
        random.shuffle(v1)
        v2 = find_min_circle(v1, [], 0)
        return v2
