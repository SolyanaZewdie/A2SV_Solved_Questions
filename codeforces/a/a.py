import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    if n <= 1:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    ptr = 1
    for _ in range(n - 1):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    def bfs(start_node):
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        queue = deque([start_node])
        farthest_node = start_node
        max_dist = 0
        
        while queue:
            curr = queue.popleft()
            if distances[curr] > max_dist:
                max_dist = distances[curr]
                farthest_node = curr
            for neighbor in adj[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)
        return farthest_node, max_dist

    u, _ = bfs(1)
    v, diameter = bfs(u)
    print(diameter * 3)

if __name__ == "__main__":
    solve()