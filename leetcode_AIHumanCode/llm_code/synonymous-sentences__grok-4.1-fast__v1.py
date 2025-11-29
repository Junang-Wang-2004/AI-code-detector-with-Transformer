import collections
import itertools
from collections import defaultdict

class Solution:
    def generateSentences(self, synonyms, text):
        unique_words = set()
        for pair in synonyms:
            unique_words.update(pair)
        
        graph = defaultdict(list)
        for a, b in synonyms:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        word_to_synonyms = {}
        
        def dfs(node, component):
            component.append(node)
            visited.add(node)
            for adj_node in graph[node]:
                if adj_node not in visited:
                    dfs(adj_node, component)
        
        for word in sorted(unique_words):
            if word not in visited:
                comp = []
                dfs(word, comp)
                sorted_synonyms = sorted(comp)
                for syn in sorted_synonyms:
                    word_to_synonyms[syn] = sorted_synonyms
        
        text_words = text.split()
        choices = []
        for word in text_words:
            if word not in word_to_synonyms:
                choices.append([word])
            else:
                choices.append(word_to_synonyms[word])
        
        return [" ".join(combo) for combo in itertools.product(*choices)]
