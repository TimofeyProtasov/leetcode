def f(nums: list) -> list:
    n = len(nums) // 2
    result = []
    for i in range(n):
        result.extend((nums[i], nums[i + n]))
    return result

print(f(list(map(int, input().split()))))