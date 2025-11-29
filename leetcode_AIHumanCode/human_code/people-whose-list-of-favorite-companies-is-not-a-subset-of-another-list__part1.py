# Time:  O(n * m * l + n^2 * m), n is favoriteCompanies.length
#                              , m is the max of favoriteCompanies[i].length
#                              , l is the max of favoriteCompanies[i][j].length
# Space: O(n * m * l)

class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        """
        lookup, comps = {}, []
        for cs in favoriteCompanies:
            comps.append(set())
            for c in cs:
                if c not in lookup:
                    lookup[c] = len(lookup)
                comps[-1].add(lookup[c])
        return [i for i, c1 in enumerate(comps)
                if not any(i != j and len(c1) < len(c2) and c1 < c2
                           for j, c2 in enumerate(comps))]
    


