from collections import deque
class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        q = deque([source])
        seen = set([source])
        while q:
            c = q.popleft()
            if c == destination :
                return True
            for n in graph[c]:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
        return False
