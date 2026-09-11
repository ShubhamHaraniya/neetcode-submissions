from collections import deque, defaultdict
from typing import List

class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        # Build adjacency list
        li = defaultdict(list)

        for u, v in edges:
            li[u].append(v)
            li[v].append(u)

        # BFS queue
        queue = deque([source])
        visited = {source}

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for neighbor in li[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False