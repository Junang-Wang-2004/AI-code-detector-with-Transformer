class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        parts = sentence.split()
        updated = []
        for token in parts:
            if token and token[0] == '$' and token[1:].isdigit():
                price = int(token[1:])
                adjusted = price * (100 - discount)
                whole = adjusted // 100
                frac = adjusted % 100
                updated.append(f"${whole}.{frac:02d}")
            else:
                updated.append(token)
        return ' '.join(updated)
