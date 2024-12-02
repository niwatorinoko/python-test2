from itertools import combinations

nums = [4, 6, 7, 8, 11, 24, 35, 37, 40, 48]
comb = list(combinations(nums, 6))

for count, data in enumerate(comb[-5:], start=len(comb)-4):
    print(f"{count}: {data}")

