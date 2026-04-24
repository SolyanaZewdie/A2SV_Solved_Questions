class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        
        graph = {i: [] for i in range(n)}
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                
                dx = x1 - x2
                dy = y1 - y2
                
                if dx * dx + dy * dy <= r1 * r1:
                    graph[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            count = 1
            
            for nei in graph[node]:
                if nei not in visited:
                    count += dfs(nei, visited)
            
            return count
        
        res = 0
        
        for i in range(n):
            visited = set()
            res = max(res, dfs(i, visited))
        
        return res