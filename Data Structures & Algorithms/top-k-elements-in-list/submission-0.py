class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        result = []
        max_value = 0
        for i in range(len(nums)):
            value = num_dict.get(nums[i],0) + 1
            num_dict[nums[i]] = value
        sorted_items = sorted(num_dict.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            kth_key, kth_val = sorted_items[i]
            result.append(kth_key)
        return result