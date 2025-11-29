class C1:

    def __init__(self):
        self.prefix = 'http://tinyurl.com/'
        self.digits = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.urls = []
        self.sequence = 0

    def encode(self, a1):
        v1 = self.sequence
        self.sequence += 1
        v2 = self._encode_id(v1)
        self.urls.append(a1)
        return self.prefix + v2

    def decode(self, a1):
        v1 = self._decode_id(a1[len(self.prefix):])
        return self.urls[v1]

    def _encode_id(self, a1):
        v1 = []
        for v2 in range(6):
            v1.append(self.digits[a1 % 62])
            a1 //= 62
        return ''.join(reversed(v1))

    def _decode_id(self, a1):
        v1 = 0
        for v2 in a1:
            v1 = v1 * 62 + self.digits.index(v2)
        return v1
