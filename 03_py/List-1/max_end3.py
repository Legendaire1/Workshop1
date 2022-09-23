def max_end3(nums):
  new_nums = nums
  larger = 0
  if(nums[0] >= nums[len(nums)-1]):
    larger = nums[0]
  else:
    larger = nums[len(nums)-1]
  for i in range(len(nums)):
    new_nums[i] = larger
  return new_nums
