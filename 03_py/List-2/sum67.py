def sum67(nums):
    total = 0
    ind = 0
    while ind < len(nums):
        if nums[ind] == 6:
            while nums[ind] != 7:
                ind += 1
        else:
            total += nums[ind]
        ind += 1
    return total
