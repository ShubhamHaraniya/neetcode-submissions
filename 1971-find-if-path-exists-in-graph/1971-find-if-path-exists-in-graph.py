class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()

        def dfs(node):
            if node == destination:
                return True
            seen.add(node)
            for n in graph[node]:
                if n  not in seen:
                    if dfs(n):
                        return True
            return False
        return dfs(source)