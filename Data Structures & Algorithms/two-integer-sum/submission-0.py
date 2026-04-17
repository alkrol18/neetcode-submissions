class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}
        complement = 0
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums_dic:
                return [nums_dic[complement],i]
            nums_dic[n] = i
