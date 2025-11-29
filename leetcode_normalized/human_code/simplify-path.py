class C1(object):

    def simplifyPath(self, a1):
        v1, v2 = ([], a1.split('/'))
        for v3 in v2:
            if v3 == '..' and v1:
                v1.pop()
            elif v3 != '..' and v3 != '.' and v3:
                v1.append(v3)
        return '/' + '/'.join(v1)
