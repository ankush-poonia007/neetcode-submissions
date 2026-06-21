class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = {}

        for i , num in enumerate(numbers,start = 1):
            comp = target - num

            if comp in freq:
                return [ freq[comp] , i ]
            
            freq[num] = i