import collections

class C1(object):

    def checkIfPrerequisite(self, a1, a2, a3):
        """
        :rtyp
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
        v4 = []
        for v5, v6 in a3:
            v7, v8 = ([v5], set([v5]))
            while v7:
                v9 = v7.pop()
                for v10 in v1[v9]:
                    if v10 in v8:
                        continue
                    v7.append(v10)
                    v8.add(v10)
            v4.append(v6 in v8)
        return v4
