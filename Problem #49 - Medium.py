# Given an array of numbers, find the maximum sum of any contiguous subarray of the array
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
# * Do this in O(N) time.

arr = [34, -50, 42, 14, -5, 86]
result = []
result_sum = 0

for i in arr:
    result_sum = result_sum + i
    if(result_sum >= 0):
        result.append(i)
    else:
        result = []
        result_sum = 0

print(result_sum)