n, k, q = map(int, input().split())
MAX_TEMP = 200001
diff = [0] * (MAX_TEMP + 2)
for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1
count = [0] * (MAX_TEMP + 2)
for i in range(1, MAX_TEMP + 1):
    count[i] = count[i - 1] + diff[i]
admissible = [0] * (MAX_TEMP + 2)
for i in range(1, MAX_TEMP + 1):
    admissible[i] = admissible[i - 1] + (1 if count[i] >= k else 0)
for _ in range(q):
    a, b = map(int, input().split())
    print(admissible[b] - admissible[a - 1])
