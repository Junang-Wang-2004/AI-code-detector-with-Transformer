class C1:

    def entityParser(self, a1: str) -> str:
        v1 = [('&frasl;', '/'), ('&quot;', '"'), ('&apos;', "'"), ('&amp;', '&'), ('&gt;', '>'), ('&lt;', '<')]
        for v2, v3 in v1:
            a1 = a1.replace(v2, v3)
        return a1
