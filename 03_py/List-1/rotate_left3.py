def rotate_left3(nums):
  new_nums = nums
  first = nums[0]
  for i in range(len(nums)-1):
    new_nums[i] = nums[i+1]
  new_nums[len(nums)-1] = first
  return new_nums
