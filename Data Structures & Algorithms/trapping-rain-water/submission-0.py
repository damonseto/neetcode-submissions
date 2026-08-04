class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        inc = 0
        max = 0
        max = 0
        count = 0
        while start < len(height) and inc < len(height):
            if inc == len(height) - 1 and height[len(height) - 1] < height[start]:
                return max
            if height[inc] >= height[start] and inc != start:
                max += count
                count = 0
                start = inc
            else:
                count += height[start] - height[inc]
            inc += 1
        return max


