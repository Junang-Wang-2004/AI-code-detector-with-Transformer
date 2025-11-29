import datetime

class C1(object):

    def daysBetweenDates(self, a1, a2):
        v1 = datetime.datetime.strptime(a1, '%Y-%m-%d')
        v1 -= datetime.datetime.strptime(a2, '%Y-%m-%d')
        return abs(v1.days)
