class Solution:
    def entityParser(self, text: str) -> str:
        subs = [
            ("&frasl;", "/"),
            ("&quot;", '"'),
            ("&apos;", "'"),
            ("&amp;", "&"),
            ("&gt;", ">"),
            ("&lt;", "<")
        ]
        for pat, subst in subs:
            text = text.replace(pat, subst)
        return text
