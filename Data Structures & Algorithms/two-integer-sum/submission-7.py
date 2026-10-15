class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]
            else: 
                seen[num] = i

# O(n) time complexity: one for loop running n times, each lookup is O(1) on average
# O(n) space complexity: in worst conditions n-1 numbers get added to the hashmap