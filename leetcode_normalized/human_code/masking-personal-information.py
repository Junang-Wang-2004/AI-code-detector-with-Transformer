class C1(object):

    def maskPII(self, a1):
        """
        """
        if '@' in a1:
            v1, v2 = a1.split('@')
            return '{}*****{}@{}'.format(v1[0], v1[-1], v2).lower()
        v3 = [x for v4 in a1 if v4.isdigit()]
        v5 = '***-***-{}'.format(v3[-4:])
        if len(v3) == 10:
            return v5
        return '+{}-{}'.format('*' * (len(v3) - 10), v5)
