# NUMBER = 0004
# TITLE = Median of Two Sorted Arrays
# FILENAME = 0004_Median_of_Two_Sorted_Arrays.py
# DIFFICULTY = hard
# LANGUAGE = python
# TAGS = Array, Binary_Search, Divide_and_Conquer
# LEETCODELINK = https://leetcode.com/problems/two-sum/
# ACCEPTANCERATE = 35.4%
# NOTES = 
# END-SRD = 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted((nums1 + nums2))
        length = arr.__len__() - 1

        ans = float(( arr[int(length/2)] + arr[int((length+1)/2)] ) / 2)

        return ans