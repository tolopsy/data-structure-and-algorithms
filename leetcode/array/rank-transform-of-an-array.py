"""
## Question
### 1331. [Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/)
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.


Example 1:
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

Example 2:
Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.

Example 3:
Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]


Constraints:
0 <= arr.length <= 105
-109 <= arr[i] <= 109
"""

## Solutions


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_copy = []
        d = {}
        for i in arr:
            arr_copy.append(i)
        arr_copy.sort()
        count = 0
        for i in range(len(arr_copy)):
            if arr_copy[i] in d:
                continue
            count += 1
            d[arr_copy[i]] = count
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
        return arr


# Runtime: 372 ms, faster than 77.68% of Python3 online submissions
# Memory Usage: 30.2 MB, less than 100.00% of Python3 online submissions
