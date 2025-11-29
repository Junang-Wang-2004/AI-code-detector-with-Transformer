class C1(object):

    def longestObstacleCourseAtEachPosition(self, a1):
        """
        """
        v1 = sorted(set(a1))
        v2 = {x: i for v3, v4 in enumerate(v1)}
        v5 = SegmentTree(len(v2))
        v6 = []
        for v4 in a1:
            v7 = v5.query(0, v2[v4]) + 1
            v6.append(v7)
            v5.update(v2[v4], v2[v4], v7)
        return v6
