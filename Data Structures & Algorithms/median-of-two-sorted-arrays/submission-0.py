class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)

        # Always binary search on the smaller array
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        
        low, high = 0, n

        while low <= high:
            mid1 = (high + low) // 2 # cut in nums1
            mid2 = (m + n + 1) // 2 - mid1 # cut in nums2 (forced)

            # Elements just left/right of cuts (handle edge cases with ±inf)
            num_left_1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            num_left_2 =  nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            num_right_1 = nums1[mid1] if mid1 < n else float("inf")
            num_right_2 = nums2[mid2] if mid2 < m else float("inf")

            if num_left_1 <= num_right_2 and num_left_2 <= num_right_1:
                # Valid partition
                maxLeft = max(num_left_1, num_left_2)
                minRight = min(num_right_1, num_right_2)
                if (n + m) % 2 == 0:
                    return (maxLeft + minRight) / 2.0
                else:
                    return float(maxLeft)
            elif num_left_1 > num_right_2:
                high = mid1 - 1 # too far right in nums1
            else:
                low = mid1 + 1 # too far left in nums1
        