n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

count_map = defaultdict(int)
left = 0
result = 0
unique_count = 0

for right in range(n):
    if count_map[a[right]] == 0:
        unique_count += 1
    count_map[a[right]] += 1

    while unique_count > k:
        count_map[a[left]] -= 1
        if count_map[a[left]] == 0:
            unique_count -= 1
        left += 1

    result += (right - left + 1)

print(result)
