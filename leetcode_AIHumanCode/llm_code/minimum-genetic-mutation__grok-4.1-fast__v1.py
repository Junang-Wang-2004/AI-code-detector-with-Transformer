from collections import deque

class Solution:
    def minMutation(self, start, end, bank):
        gene_bank = set(bank)
        seen = set([start])
        bfs = deque([(start, 0)])
        while bfs:
            current_gene, mutations = bfs.popleft()
            if current_gene == end:
                return mutations
            for position in range(len(current_gene)):
                original_nuc = current_gene[position]
                for nucleotide in 'ATCG':
                    if nucleotide == original_nuc:
                        continue
                    gene_list = list(current_gene)
                    gene_list[position] = nucleotide
                    next_gene = ''.join(gene_list)
                    if next_gene in gene_bank and next_gene not in seen:
                        seen.add(next_gene)
                        bfs.append((next_gene, mutations + 1))
        return -1
