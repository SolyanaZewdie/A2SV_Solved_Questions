import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    h = int(input_data[idx])
    w = int(input_data[idx + 1])
    idx += 2
    
    grid = []
    for _ in range(h):
        grid.append(input_data[idx])
        idx += 1
        
    prefH = [[0] * (w + 1) for _ in range(h + 1)]
    prefV = [[0] * (w + 1) for _ in range(h + 1)]
    
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            h_val = 1 if (j < w and grid[i-1][j-1] == '.' and grid[i-1][j] == '.') else 0
            v_val = 1 if (i < h and grid[i-1][j-1] == '.' and grid[i][j-1] == '.') else 0
            
            prefH[i][j] = h_val + prefH[i-1][j] + prefH[i][j-1] - prefH[i-1][j-1]
            prefV[i][j] = v_val + prefV[i-1][j] + prefV[i][j-1] - prefV[i-1][j-1]
            
    q = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(q):
        r1 = int(input_data[idx])
        c1 = int(input_data[idx + 1])
        r2 = int(input_data[idx + 2])
        c2 = int(input_data[idx + 3])
        idx += 4
        
        total = 0
        if c2 > c1:
            total += (prefH[r2][c2-1] - prefH[r1-1][c2-1] - prefH[r2][c1-1] + prefH[r1-1][c1-1])
        if r2 > r1:
            total += (prefV[r2-1][c2] - prefV[r1-1][c2] - prefV[r2-1][c1-1] + prefV[r1-1][c1-1])
            
        results.append(str(total))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()