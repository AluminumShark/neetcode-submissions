class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[b].append(a)

        state = [0] * numCourses

        def dfs(course: int) -> bool:
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for nei in adj[course]:
                if not dfs(nei):
                    return False

            state[course] = 2
            return True

        for c in range(numCourses):
            if state[c] == 0:
                if not dfs(c):
                    return False
        
        return True
