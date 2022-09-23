def sum2(nums):
  sum = 0
  if len(nums) < 3:
    for i in nums:
      sum += i
    return sum
  else:
    j = 0
    while j < 2:
      sum+= nums[j]
      j += 1
    return sum
