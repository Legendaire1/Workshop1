def array123(nums):
  counter = 0
  while counter < len(nums) - 2:
    if nums[counter] == 1 and nums[counter + 1] == 2 and nums[counter + 2] == 3:
      return True
    counter += 1
  return False
