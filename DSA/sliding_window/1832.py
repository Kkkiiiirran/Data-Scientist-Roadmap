def maxFrequency(nums, k):
    ans = left = target = cumm = 0
    nums.sort()

    for right in range(len(nums)):
        target = nums[right]
        cumm+= target

        while((right-left+1)*target-cumm > k):
            cumm-=nums[left]
            left+=1

        ans = max(ans, right-left+1)
    
    return ans

print(maxFrequency([1, 2, 3, 4, 4, 12], 4))
