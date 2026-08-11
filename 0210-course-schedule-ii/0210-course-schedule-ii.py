class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        UNVISITED, VISITING, VISITED = 0,1,2

        v  = [UNVISITED] *  numCourses

        order = []

        def dfs(node):
            if v[node] == VISITING: return False 
            elif v[node] == VISITED: return True 

            v[node] = VISITING 

            for n in graph[node]:
                if not dfs(n):
                    return False 
            order.append(node)
            v[node] = VISITED
            return True 

        for n in range(numCourses):
            if not dfs(n):
                return []

        return order