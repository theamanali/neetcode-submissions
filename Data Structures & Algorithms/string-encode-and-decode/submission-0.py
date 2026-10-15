class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []

        for word in strs:
            pieces.append(str(len(word)) + "#" + word)
        
        return "".join(pieces)



    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            word_length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + word_length

            decoded.append(s[word_start:word_end])
            
            i = word_end
        
        return decoded

                
            



