# Nice — let’s step up the difficulty a bit. Here’s a classic sliding-window variant that appears in interviews at FAANG:

# 🔥 Question 4 — Longest Subarray with At Most K Distinct Elements

# Type: variable-size sliding window + hashmap (frequency)
# Difficulty: Medium — good for Google/Amazon

# Problem

# Given an integer array nums and an integer k, return the length of the longest contiguous subarray that contains at most k distinct integers.

# Function signature
# def longest_subarray_k_distinct(nums: List[int], k: int) -> int:
#     pass

# Examples
# Input: nums = [1,2,1,2,3], k = 2
# Output: 4     # [1,2,1,2]

# Input: nums = [1,2,1,3,4], k = 3
# Output: 4     # [1,2,1,3] or [2,1,3,4]

# Input: nums = [4,4,4,4], k = 1
# Output: 4