class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []

        for num in nums:
            idx = abs(num) - 1 # 4-1=3

            if nums[idx] < 0:
                output.append(idx + 1)
            nums[idx] = -nums[idx]
        
        return output
        