from collections import deque, defaultdict

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

    def sortItems(self, n, m, group, beforeItems):
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        item_adj = [[] for _ in range(n)]
        item_in_degree = [0] * n
        group_adj = [[] for _ in range(group_id)]
        group_in_degree = [0] * group_id
        
        for i in range(n):
            for prev in beforeItems[i]:
                item_adj[prev].append(i)
                item_in_degree[i] += 1
                if group[prev] != group[i]:
                    group_adj[group[prev]].append(group[i])
                    group_in_degree[group[i]] += 1
        
        def topo_sort(nodes, adj, in_degree):
            queue = deque([u for u in nodes if in_degree[u] == 0])
            res = []
            while queue:
                u = queue.popleft()
                res.append(u)
                for v in adj[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            return res if len(res) == len(nodes) else []

        item_order = topo_sort(range(n), item_adj, item_in_degree)
        group_order = topo_sort(range(group_id), group_adj, group_in_degree)
        
        if not item_order or not group_order:
            return []
        
        items_in_group = defaultdict(list)
        for item in item_order:
            items_in_group[group[item]].append(item)
            
        res = []
        for g in group_order:
            res.extend(items_in_group[g])
            
        return res