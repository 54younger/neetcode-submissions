class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums_dict.get(target-nums[i]) == None:
                nums_dict[nums[i]] = i
            else:
                return [nums_dict[target-nums[i]], i]
        