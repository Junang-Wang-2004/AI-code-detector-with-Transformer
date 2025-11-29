class Solution:
    def peopleIndexes(self, favoriteCompanies):
        company_id = {}
        next_id = 0
        sorted_ids = []
        for companies in favoriteCompanies:
            unique_ids = []
            for company in companies:
                if company not in company_id:
                    company_id[company] = next_id
                    next_id += 1
                unique_ids.append(company_id[company])
            sorted_ids.append(sorted(set(unique_ids)))
        
        def strict_subset(small, large):
            if len(small) >= len(large):
                return False
            i = j = 0
            while i < len(small) and j < len(large):
                if small[i] == large[j]:
                    i += 1
                    j += 1
                elif small[i] < large[j]:
                    return False
                else:
                    j += 1
            return i == len(small)
        
        num_people = len(sorted_ids)
        result = []
        for p in range(num_people):
            covered = False
            for q in range(num_people):
                if p == q or len(sorted_ids[q]) <= len(sorted_ids[p]):
                    continue
                if strict_subset(sorted_ids[p], sorted_ids[q]):
                    covered = True
                    break
            if not covered:
                result.append(p)
        return result
