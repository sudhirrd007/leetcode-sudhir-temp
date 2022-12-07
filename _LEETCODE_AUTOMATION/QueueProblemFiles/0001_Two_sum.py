# NUMBER = 0001
# TITLE = Two Sum
# FILENAME = 0001_Two_sum.py
# DIFFICULTY = easy
# LANGUAGE = python
# TAGS = ARRAY, HASHTABLE
# LEETCODELINK = https://leetcode.com/problems/two-sum/
# ACCEPTANCERATE = 49.1%
# NOTES = 
# END-SRD = 

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(nums.__len__()):
            for j in range(nums.__len__()):
                if(i<j):
                    if((nums[i] +nums[j]) == target ):
                        return [i,j]
                        