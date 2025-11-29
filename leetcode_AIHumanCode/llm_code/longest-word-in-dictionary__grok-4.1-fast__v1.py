class Solution:
    def longestWord(self, words):
        root = {}
        for term in words:
            curr_node = root
            for letter in term:
                curr_node = curr_node.setdefault(letter, {})
            curr_node["#"] = term
        
        result = [""]
        
        def explore(nd):
            if "#" in nd:
                candidate = nd["#"]
                if (len(candidate) > len(result[0]) or
                    (len(candidate) == len(result[0]) and candidate < result[0])):
                    result[0] = candidate
                for key in nd:
                    if key != "#":
                        explore(nd[key])
        
        for child in root.values():
            explore(child)
        
        return result[0]
