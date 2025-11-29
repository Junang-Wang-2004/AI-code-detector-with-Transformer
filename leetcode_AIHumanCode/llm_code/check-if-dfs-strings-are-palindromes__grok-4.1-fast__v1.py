class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)
        seq = []
        bounds = [None] * n
        
        def traverse(node):
            begin = len(seq)
            for kid in tree[node]:
                traverse(kid)
            seq.append(s[node])
            bounds[node] = (begin, len(seq) - 1)
        
        traverse(0)
        
        def compute_radii(chars):
            transformed = '^#' + '#'.join(chars) + '#$'
            rad = [0] * len(transformed)
            cent, rad_bound = 0, 0
            for pos in range(1, len(transformed) - 1):
                refl = 2 * cent - pos
                if pos < rad_bound:
                    rad[pos] = min(rad_bound - pos, rad[refl])
                while transformed[pos + rad[pos] + 1] == transformed[pos - rad[pos] - 1]:
                    rad[pos] += 1
                if pos + rad[pos] > rad_bound:
                    cent, rad_bound = pos, pos + rad[pos]
            return rad
        
        radii = compute_radii(seq)
        ans = []
        for i in range(n):
            start, finish = bounds[i]
            center_pos = start + finish + 2
            sub_len = finish - start + 1
            ans.append(radii[center_pos] >= sub_len)
        return ans
