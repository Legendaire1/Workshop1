def reverse3(nums):
  new_nums = nums
  first = nums[0]
  for i in range(len(nums)):
    new_nums[i] = nums[len(nums)-1-i]
  new_nums[len(nums)-1] = first
  return nums
