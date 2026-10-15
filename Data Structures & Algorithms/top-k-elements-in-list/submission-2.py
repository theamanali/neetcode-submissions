class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        for num, count in num_counts.items():
            freq[count].append(num)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for nums in freq[i]:
                result.append(nums)
            if len(result) == k:
                return result


        