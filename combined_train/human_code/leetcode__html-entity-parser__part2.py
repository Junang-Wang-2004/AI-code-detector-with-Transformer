class C1(object):

    def entityParser(self, a1):
        """
        """
        v1 = ['&quot;', '&apos;', '&amp;', '&gt;', '&lt;', '&frasl;']
        v2 = ['"', "'", '&', '>', '<', '/']
        v3 = []
        v4, v5 = (0, 0)
        while v4 != len(a1):
            if a1[v4] != '&':
                v3.append(a1[v4])
                v4 += 1
            else:
                for v5, v6 in enumerate(v1):
                    if v6 == a1[v4:v4 + len(v6)]:
                        v3.append(v2[v5])
                        v4 += len(v6)
                        break
                else:
                    v3.append(a1[v4])
                    v4 += 1
        return ''.join(v3)
