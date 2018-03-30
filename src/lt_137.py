"""
https://leetcode.com/problems/single-number-ii

Related
  - lt_136_single-number
  - lt_260_single-number-iii
"""

"""
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 
"""

import collections

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # https://shenjie1993.gitbooks.io/leetcode-python/137%20Single%20Number%20II.html
        #ans = 0
        #for i in range(32):
        #    count = 0
        #    for n in nums:
        #        count += (n >> i) & 1
        #    ans |= (count % 3) << i
        #return ans
        result = 0
        for i in range(32):
            count = 0
            for n in nums:
                count += (n >> i) & 1
            count %= 3
            # handling negative situation
            if i == 31 and count:
                result -= 1 << 31
            else:
                result |= count << i
        return result

    def singleNumber_hashtable(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        records = collections.defaultdict(int)
        for n in nums:
            records[n] += 1
            if records[n] == 3: records.pop(n)
        return list(records.keys())[0]

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 2, 2, 3, 3, 3], 1),
        ([-2,-2,1,1,-3,1,-3,-3,-4,-2], -4),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().singleNumber(test_case[0])
        print('output:', output)
        assert output == test_case[1]

