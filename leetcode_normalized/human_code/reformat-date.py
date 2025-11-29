class C1(object):

    def reformatDate(self, a1):
        """
        """
        v1 = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        return '{:04d}-{:02d}-{:02d}'.format(int(a1[-4:]), v1[a1[-8:-5]], int(a1[:a1.index(' ') - 2]))
