class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}

        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        ordered = sorted(num_counts, key=num_counts.get, reverse=True)

        return ordered[:k]

        