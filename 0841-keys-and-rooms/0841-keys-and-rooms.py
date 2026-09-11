from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque(rooms[0])
        v = set()

        while q:
            c = q.popleft()
            if c not in v:
                q.extend(rooms[c])
            v.add(c)
        
        for k in range(1,len(rooms)):
            if k not in v:
                return False
        
        return True