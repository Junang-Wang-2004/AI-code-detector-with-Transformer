class C1(object):

    def canAttendMeetings(self, a1):
        """
        """
        a1.sort(key=lambda x: x[0])
        for v1 in range(1, len(a1)):
            if a1[v1][0] < a1[v1 - 1][1]:
                return False
        return True
