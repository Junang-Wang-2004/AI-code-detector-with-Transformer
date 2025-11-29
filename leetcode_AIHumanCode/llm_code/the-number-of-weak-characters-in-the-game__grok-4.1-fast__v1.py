class Solution:
    def numberOfWeakCharacters(self, properties):
        properties.sort(key=lambda x: -x[0])
        res = 0
        max_def = 0
        i = 0
        n = len(properties)
        while i < n:
            atk = properties[i][0]
            grp_cnt = 0
            grp_max = 0
            while i < n and properties[i][0] == atk:
                df = properties[i][1]
                if df < max_def:
                    grp_cnt += 1
                grp_max = max(grp_max, df)
                i += 1
            res += grp_cnt
            max_def = max(max_def, grp_max)
        return res
