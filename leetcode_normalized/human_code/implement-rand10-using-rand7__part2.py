class C1(object):

    def rand10(self):
        """
        """
        while True:
            v1 = (rand7() - 1) * 7 + (rand7() - 1)
            if v1 < 40:
                return v1 % 10 + 1
