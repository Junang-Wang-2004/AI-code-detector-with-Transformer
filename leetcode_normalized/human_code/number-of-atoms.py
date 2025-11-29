import collections
import re

class C1(object):

    def countOfAtoms(self, a1):
        """
        """
        v1 = re.findall('([A-Z][a-z]*)(\\d*)|(\\()|(\\))(\\d*)', a1)
        v2 = [collections.Counter()]
        for v3, v4, v5, v6, v7 in v1:
            if v3:
                v2[-1][v3] += int(v4 or 1)
            if v5:
                v2.append(collections.Counter())
            if v6:
                v8 = v2.pop()
                for v9, v10 in v8.items():
                    v2[-1][v9] += v10 * int(v7 or 1)
        return ''.join((v3 + (str(v2[-1][v3]) if v2[-1][v3] > 1 else '') for v3 in sorted(v2[-1])))
