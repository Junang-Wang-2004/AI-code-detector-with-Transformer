class C1:

    def __init__(self, a1, a2, a3):
        self.enc_map = {}
        v1 = len(a1)
        for v2 in range(v1):
            self.enc_map[a1[v2]] = a2[v2]
        self.match_count = {}
        for v3 in a3:
            v4 = self.make_encoded(v3)
            v5 = self.match_count.get(v4, 0)
            self.match_count[v4] = v5 + 1

    def make_encoded(self, a1):
        v1 = []
        for v2 in a1:
            if v2 not in self.enc_map:
                return ''
            v1.append(self.enc_map[v2])
        return ''.join(v1)

    def encrypt(self, a1):
        return self.make_encoded(a1)

    def decrypt(self, a1):
        return self.match_count.get(a1, 0)
