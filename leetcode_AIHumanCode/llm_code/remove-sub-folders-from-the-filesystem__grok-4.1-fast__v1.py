class Solution:
    def removeSubfolders(self, folder):
        root = {}
        for p in folder:
            parts = p.split('/')[1:]
            node = root
            for part in parts:
                node = node.setdefault(part, {})
            node['$'] = True
        res = []
        def search(nd, trail):
            if '$' in nd:
                res.append('/' + '/'.join(trail))
                return
            for k in nd:
                if k == '$':
                    continue
                trail.append(k)
                search(nd[k], trail)
                trail.pop()
        search(root, [])
        return res
