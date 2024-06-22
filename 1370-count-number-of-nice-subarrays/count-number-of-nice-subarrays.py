class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        current_sum = 0
        result = 0
        
        for num in nums:
            if num % 2 == 1:
                current_sum += 1
            
            if current_sum - k in prefix_sums:
                result += prefix_sums[current_sum - k]
            
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
        
        return result