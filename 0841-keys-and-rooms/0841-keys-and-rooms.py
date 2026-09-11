from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        v = {0}

        while q:
            c = q.popleft()

            for key in rooms[c]:
                if key not in v:
                    v.add(key)
                    q.append(key)

        return len(v) == len(rooms)