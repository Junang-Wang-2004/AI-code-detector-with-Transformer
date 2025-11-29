import collections

class C1(object):

    def findAllPeople(self, a1, a2, a3):
        """
        """
        a2.sort(key=lambda x: x[2])
        v1 = {0, a3}
        v2 = collections.defaultdict(list)
        for v3, (v4, v5, v6) in enumerate(a2):
            v2[v4].append(v5)
            v2[v5].append(v4)
            if v3 + 1 != len(a2) and a2[v3 + 1][2] == a2[v3][2]:
                continue
            v7 = [v3 for v3 in v2.keys() if v3 in v1]
            while v7:
                v8 = []
                for v9 in v7:
                    for v10 in v2[v9]:
                        if v10 in v1:
                            continue
                        v1.add(v10)
                        v8.append(v10)
                v7 = v8
            v2 = collections.defaultdict(list)
        return list(v1)
