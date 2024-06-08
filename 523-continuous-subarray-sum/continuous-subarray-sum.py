from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        mod_dict = {0: -1}  # To handle the case where the subarray starts from the beginning
        
        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k
            
            if mod in mod_dict:
                if i - mod_dict[mod] >= 2:  # Ensure the subarray length is at least 2
                    return True
            else:
                mod_dict[mod] = i
        
        return False
