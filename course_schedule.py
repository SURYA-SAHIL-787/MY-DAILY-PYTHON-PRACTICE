from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
            
        # visit status: 0 = unvisited, 1 = visiting (in current path), 2 = visited
        visit = [0] * numCourses
        
        def dfs(crs):
            if visit[crs] == 1:
                return False
            if visit[crs] == 2:
                return True
            
            visit[crs] = 1
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visit[crs] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
