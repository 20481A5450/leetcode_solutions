class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort both arrays
        nums1.sort()
        nums2.sort()

        # List to store the result
        result = []

        # Two pointers to iterate through both arrays
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                # If elements are equal, add to the result list
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                # If nums1's element is smaller, move pointer i
                i += 1
            else:
                # If nums2's element is smaller, move pointer j
                j += 1

        return result