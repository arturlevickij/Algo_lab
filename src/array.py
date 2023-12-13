def monotton_array(nums):
    if len(nums) < 1:
        return False

    if len(nums) == 1:
        return True

    if nums[1] <= nums[1-1] and nums[0] >= nums[-1]:
        for i in range(1, len(nums)):
                pointer = nums[i]
                j = i - 1
                if j >= 0 and pointer > nums[j]:
                    return False
                nums[j+1] = pointer
                if i == (len(nums)-1):
                    return True

    else:
        for i in range(1, len(nums)):
                pointer = nums[i]
                j = i - 1
                if j >= 0 and pointer < nums[j]:
                    return False
                nums[j+1] = pointer
                if i == (len(nums)-1):
                    return True

lis = [2,2,2,2]

print(monotton_array(lis))

