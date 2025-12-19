def f(nums: list) -> list[int] | None:
    arr = len(nums) * [0]
    for elem in nums:
        arr[elem - 1] += 1

    dupl = -1
    miss = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            miss = i + 1
        if arr[i] == 2:
            dupl = i + 1
    return [dupl, miss]

print(f(list(map(int, input().split()))))