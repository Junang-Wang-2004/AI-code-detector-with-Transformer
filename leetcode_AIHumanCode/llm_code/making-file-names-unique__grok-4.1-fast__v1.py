class Solution:
    def getFolderNames(self, names):
        occupied = set()
        trackers = {}
        output = []
        for base in names:
            attempt = trackers.get(base, 0)
            suggestion = base if attempt == 0 else f"{base}({attempt})"
            while suggestion in occupied:
                attempt += 1
                suggestion = f"{base}({attempt})"
            output.append(suggestion)
            occupied.add(suggestion)
            trackers[base] = attempt + 1
        return output
