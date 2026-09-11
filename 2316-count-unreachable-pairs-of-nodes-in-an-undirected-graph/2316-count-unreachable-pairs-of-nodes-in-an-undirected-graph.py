from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            size = 1

            for nei in graph[node]:
                size += dfs(nei)

            return size

        ans = 0
        seen_nodes = 0

        for node in range(n):
            if node not in visited:
                component_size = dfs(node)
                ans += component_size * seen_nodes
                seen_nodes += component_size

        return ans