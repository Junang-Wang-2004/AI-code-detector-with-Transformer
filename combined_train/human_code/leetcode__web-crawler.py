class C1(object):

    def getUrls(self, a1):
        """
       """
        pass

class C2(object):

    def crawl(self, a1, a2):
        """
        """
        v1 = 'http://'

        def hostname(a1):
            v1 = a1.find('/', len(v1))
            if v1 == -1:
                return a1
            return a1[:v1]
        v2 = [a1]
        v3 = set(v2)
        for v4 in v2:
            v5 = hostname(v4)
            for v6 in a2.getUrls(v4):
                if v6 not in v3 and v5 == hostname(v6):
                    v2.append(v6)
                    v3.add(v6)
        return v2
