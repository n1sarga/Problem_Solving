'''Problem Link: https://leetcode.com/problems/two-sum/description/'''

def two_sum (nums, target):
    for i in range (len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sum(nums=[3, 3], target=6))