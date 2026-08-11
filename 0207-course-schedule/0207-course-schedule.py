class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        UNVISITED, VISITING, VISITED = 0,1,2

        v  = [UNVISITED] *  numCourses

        def dfs(node):
            if v[node] == VISITING: return False 
            elif v[node] == VISITED: return True 

            v[node] = VISITING 

            for n in graph[node]:
                if not dfs(n):
                    return False 
            
            v[node] = VISITED
            return True 

        for n in range(numCourses):
            if not dfs(n):
                return False 

        return True  