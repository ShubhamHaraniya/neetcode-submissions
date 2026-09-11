from collections import deque
class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        li = defaultdict(list)
        for edge in edges:
            li[edge[0]].append(edge[1])
            li[edge[1]].append(edge[0])
        visited = set()

        def dfs(s):
            if s == destination:
                return True

            visited.add(s)

            for node in li[s]:
                if node not in visited:
                    if dfs(node):
                        return True

            return False

        return dfs(source)