<<<<<<< HEAD
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n  - 1
        i , j = m -1 , n - 1
        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
=======
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n  - 1
        i , j = m -1 , n - 1
        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
>>>>>>> bea3ef94151ca3d6990b13720d2f7762e5f36c24
            k -= 1