class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                output.append(idx+1)
        return output