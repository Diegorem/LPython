def devolver_distintos(*args):
    nums = []
    for arg in args:
        nums.append(arg)

    nums = sorted(nums)
    if sum(nums) > 15:
        return nums[2]
    elif sum(nums) < 15:
        return nums[0]
    else:
        return nums[1]

print(devolver_distintos(3,7,1))