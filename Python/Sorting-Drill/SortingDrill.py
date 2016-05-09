
def sort(nums):
    for num in range(len(nums)-1, 0, -1):
        for i in range(num):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

nums = [67, 45, 2, 13, 1, 988]
print('before: ', nums)
sort(nums)
print('after: ', nums)
