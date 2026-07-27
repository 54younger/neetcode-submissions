class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0
        while start != end:
            if ((end-start) * min(heights[end], heights[start])) > max_area:
                max_area = (end-start) * min(heights[end], heights[start])
            if heights[end] < heights[start]:
                end -= 1
            elif heights[end] >= heights[start]:
                start += 1
        
        return max_area