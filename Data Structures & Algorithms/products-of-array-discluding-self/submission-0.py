class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[0])
            else:
                prefix.append(nums[i]*prefix[i-1])
        
        for i in range(len(nums)):
            if i == 0:
                suffix.append(nums[len(nums)-1-i])
            else:
                suffix.append(nums[len(nums)-1-i]*suffix[i-1])
        
        res = [suffix[len(nums)-2]]
        for i in range(1, len(nums)-1):
            res.append(prefix[i-1] * suffix[len(nums)-2-i])
        
        res.append(prefix[len(nums)-2])

        return res