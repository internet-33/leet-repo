class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        output = []

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                output.append(i)
            else:
                hashmap[i] = 1
        
        return output
        