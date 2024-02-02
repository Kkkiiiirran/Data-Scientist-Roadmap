# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # nums = nums[-k:] + nums[:-k]
    # return nums
    # print(nums)
    # print(nums[-k:])
    # print(nums[:-k])

time: O(n)
space: O(1)
