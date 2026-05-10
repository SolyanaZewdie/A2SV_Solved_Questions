class Solution(object):
    def getAncestors(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            
        res = [[] for _ in range(n)]
        
        def dfs(start_node, current_node, visited):
            visited[current_node] = True
            for neighbor in adj[current_node]:
                if not visited[neighbor]:
                    res[neighbor].append(start_node)
                    dfs(start_node, neighbor, visited)
        
        for i in range(n):
            dfs(i, i, [False] * n)
            
        return res