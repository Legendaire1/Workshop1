def centered_average(nums):
    ans = 0
    high = nums[0]
    low = nums[0]
    for n in nums:
        ans += n
        high = max(n, high)
        low = min(n, low)
    return (ans - high - low)/(len(nums)-2)