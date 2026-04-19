class Solution:
    def area_func(self, x_1, x_2, y_1, y_2):
        height = min(y_1, y_2)
        return abs(x_2-x_1) * height

    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            area = self.area_func(l, r, heights[l], heights[r])
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area