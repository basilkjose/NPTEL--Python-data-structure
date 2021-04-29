"""Given an array of integers nums and an integer target, return 
indices of the two numbers such that they add up to target."""

def twoSum( nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []