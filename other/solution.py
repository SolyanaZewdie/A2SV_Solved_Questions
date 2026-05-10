import sys
from collections import deque
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    names = input_data[1:]
    
    adj = [[] for _ in range(26)]
    in_degree = [0] * 26
    
    for i in range(n - 1):
        s1 = names[i]
        s2 = names[i+1]
        min_len = min(len(s1), len(s2))
        found_diff = False
        for j in range(min_len):
            if s1[j] != s2[j]:
                u, v = ord(s1[j]) - 97, ord(s2[j]) - 97
                adj[u].append(v)
                in_degree[v] += 1
                found_diff = True
                break
        if not found_diff and len(s1) > len(s2):
            print("Impossible")
            return
 
    queue = deque([i for i in range(26) if in_degree[i] == 0])
    res = []
    while queue:
        u = queue.popleft()
        res.append(chr(u + 97))
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(res) < 26:
        print("Impossible")
    else:
        print("".join(res))
 
if __name__ == "__main__":
    solve()