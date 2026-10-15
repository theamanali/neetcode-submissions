class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            letter_counts = [0] * 26
            for char in word:
                letter_counts[ord(char) - ord("a")] += 1
            key = tuple(letter_counts)

            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        
        return list(groups.values())