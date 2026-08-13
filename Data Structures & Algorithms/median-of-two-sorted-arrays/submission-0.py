class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        L, R = 0, m - 1
        half = (m + n) // 2
        while True:
            mid = (L + R) // 2
            j = half - mid - 2
            L_parti_A = nums1[mid] if mid >= 0 else float("-infinity")
            L_parti_B = nums2[j] if j >= 0 else float("-infinity")
            R_parti_A = nums1[mid + 1] if mid + 1 < m else float("infinity")
            R_parti_B = nums2[j + 1] if j + 1 < n else float("infinity")

            if L_parti_A <= R_parti_B and L_parti_B <= R_parti_A:
                break
            elif L_parti_A > R_parti_B:
                R = mid - 1
            elif L_parti_B > R_parti_A:
                L = mid + 1

        if (m + n) % 2 == 0:
            return (max(L_parti_A, L_parti_B) + min(R_parti_B, R_parti_A)) / 2
        return min(R_parti_A, R_parti_B)