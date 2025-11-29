class C1(object):

    def strongPasswordCheckerII(self, a1):
        """
        """
        v1 = set('!@#$%^&*()-+')
        return len(a1) >= 8 and any((c.islower() for v2 in a1)) and any((v2.isupper() for v2 in a1)) and any((v2.isdigit() for v2 in a1)) and any((v2 in v1 for v2 in a1)) and all((a1[i] != a1[i + 1] for v3 in range(len(a1) - 1)))
