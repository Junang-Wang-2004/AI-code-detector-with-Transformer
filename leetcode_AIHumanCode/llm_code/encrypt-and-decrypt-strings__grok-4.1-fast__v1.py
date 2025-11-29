class Encrypter:

    def __init__(self, chars, codes, words):
        self.enc_map = {}
        map_count = len(chars)
        for pos in range(map_count):
            self.enc_map[chars[pos]] = codes[pos]
        self.match_count = {}
        for entry in words:
            encoded = self.make_encoded(entry)
            prev = self.match_count.get(encoded, 0)
            self.match_count[encoded] = prev + 1

    def make_encoded(self, text):
        chunks = []
        for letter in text:
            if letter not in self.enc_map:
                return ""
            chunks.append(self.enc_map[letter])
        return "".join(chunks)

    def encrypt(self, plain):
        return self.make_encoded(plain)

    def decrypt(self, cipher):
        return self.match_count.get(cipher, 0)
