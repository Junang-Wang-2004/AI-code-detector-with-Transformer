class C1(object):

    def nextClosestTime(self, a1):
        """
        """
        v1, v2 = a1.split(':')
        v3 = int(v1) * 60 + int(v2)
        v4 = None
        for v5 in range(v3 + 1, v3 + 1441):
            v6 = v5 % 1440
            v1, v2 = (v6 // 60, v6 % 60)
            v4 = '%02d:%02d' % (v1, v2)
            if set(v4) <= set(a1):
                break
        return v4
