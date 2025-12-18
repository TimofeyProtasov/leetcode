def f(nums: list) -> int:
    max_one_cons = 0
    current_one_cons = 0
    for num in nums:
        if num == 1:
            current_one_cons += 1
            if current_one_cons > max_one_cons:
                max_one_cons = current_one_cons
        else:
            current_one_cons = 0
    return max_one_cons

print(f(list(map(int, input().split()))))