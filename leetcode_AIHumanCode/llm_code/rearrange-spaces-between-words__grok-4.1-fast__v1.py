class Solution:
    def reorderSpaces(self, text):
        words = text.split()
        total_spaces = len(text) - sum(len(w) for w in words)
        num_words = len(words)
        spaces_between = total_spaces // (num_words - 1) if num_words > 1 else 0
        remaining_spaces = total_spaces - spaces_between * max(num_words - 1, 0)
        separator = ' ' * spaces_between
        return separator.join(words) + ' ' * remaining_spaces
