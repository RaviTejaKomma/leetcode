__author__ = 'Ravi Teja Komma'


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]] + [0]*(len(nums) - 1)
        arr2 = [0]*(len(nums) - 1) + [nums[-1]]
        for i in range(1, len(nums)):
            arr1[i] = arr1[i-1]*nums[i]
        for i in range(len(nums)-2, -1, -1):
            arr2[i] = arr2[i+1]*nums[i]
        result = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = arr2[i+1]
            elif i == len(nums) - 1:
                result[i] = arr1[i-1]
            else:
                result[i] = arr1[i-1]*arr2[i+1]
        return result