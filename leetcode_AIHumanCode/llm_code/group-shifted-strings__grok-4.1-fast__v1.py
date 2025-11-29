class Solution(object):
    def groupStrings(self, strings):
        partitions = {}
        for entry in strings:
            start_ord = ord(entry[0])
            pattern = tuple((ord(char) - start_ord) % 26 for char in entry)
            partitions.setdefault(pattern, []).append(entry)
        return [sorted(items) for items in partitions.values()]
