class C1:

    def removeSubfolders(self, a1):
        v1 = {}
        for v2 in a1:
            v3 = v2.split('/')[1:]
            v4 = v1
            for v5 in v3:
                v4 = v4.setdefault(v5, {})
            v4['$'] = True
        v6 = []

        def search(a1, a2):
            if '$' in a1:
                v6.append('/' + '/'.join(a2))
                return
            for v1 in a1:
                if v1 == '$':
                    continue
                a2.append(v1)
                search(a1[v1], a2)
                a2.pop()
        search(v1, [])
        return v6
