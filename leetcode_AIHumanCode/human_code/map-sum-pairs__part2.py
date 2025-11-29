        # Time: O(n)
        curr = self.__root
        for c in key:
            curr = curr[c]
        delta = val
        if "_end" in curr:
            delta -= curr["_end"]

        curr = self.__root
        for c in key:
            curr = curr[c]
            if "_count" in curr:
                curr["_count"] += delta
            else:
                curr["_count"] = delta
        curr["_end"] = val


    def sum(self, prefix):
        """
        """
