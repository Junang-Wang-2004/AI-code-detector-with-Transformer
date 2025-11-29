import string

class C1(object):

    def validIPAddress(self, a1):
        """
        """
        v1 = a1.split('.')
        if len(v1) == 4:
            for v2 in range(len(v1)):
                if not v1[v2].isdigit() or not 0 <= int(v1[v2]) < 256 or (v1[v2][0] == '0' and len(v1[v2]) > 1):
                    return 'Neither'
            return 'IPv4'
        v1 = a1.split(':')
        if len(v1) == 8:
            for v2 in range(len(v1)):
                if not 1 <= len(v1[v2]) <= 4 or not all((c in string.hexdigits for v3 in v1[v2])):
                    return 'Neither'
            return 'IPv6'
        return 'Neither'
