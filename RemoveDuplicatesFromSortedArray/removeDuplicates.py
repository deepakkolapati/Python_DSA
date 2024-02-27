def removeDuplicates(nums: list[int]) -> int:
        length = len(nums)
        if length<=1:
            return length
        unique_nums = [nums[0]]
        unique_nums.extend([nums[i]  for i in range(1,length) if nums[i]!=nums[i-1]] )
        nums[:] = unique_nums
        return len(nums)

if __name__=="__main__":
    nums=[1,1,2,3,4,4,4,4,5,5,5,8,8,8,10,11,11,13,17,17,19,20]
    removeDuplicates(nums)
    print(nums)