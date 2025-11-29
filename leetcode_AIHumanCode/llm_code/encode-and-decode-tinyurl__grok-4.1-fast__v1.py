class Codec:
    def __init__(self):
        self.prefix = "http://tinyurl.com/"
        self.digits = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.urls = []
        self.sequence = 0

    def encode(self, url):
        identifier = self.sequence
        self.sequence += 1
        short = self._encode_id(identifier)
        self.urls.append(url)
        return self.prefix + short

    def decode(self, short):
        identifier = self._decode_id(short[len(self.prefix):])
        return self.urls[identifier]

    def _encode_id(self, num):
        parts = []
        for _ in range(6):
            parts.append(self.digits[num % 62])
            num //= 62
        return ''.join(reversed(parts))

    def _decode_id(self, short):
        val = 0
        for ch in short:
            val = val * 62 + self.digits.index(ch)
        return val
