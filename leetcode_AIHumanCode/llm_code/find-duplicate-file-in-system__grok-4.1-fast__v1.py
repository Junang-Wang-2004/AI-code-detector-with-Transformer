import collections

class Solution:
    def findDuplicate(self, paths):
        content_groups = collections.defaultdict(list)
        for entry in paths:
            parts = entry.split()
            root = parts[0]
            for part in parts[1:]:
                name_part, remainder = part.split('(', 1)
                text, _ = remainder.split(')', 1)
                content_groups[text].append(f"{root}/{name_part}")
        return [group for group in content_groups.values() if len(group) > 1]
