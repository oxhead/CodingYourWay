"""
https://leetcode.com/problems/heaters

Related:
"""

"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

    Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
    Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
    As long as a house is in the heaters' warm radius range, it can be warmed.
    All the heaters follow your radius standard and the warm radius will the same.

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""

class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # Time: O(max(mlogm, nlogn)), O(m + n) for the calculation
        # Space: O(1)
        houses.sort()
        heaters.sort()
        min_radius = 0
        i = 0
        for house in houses:
            # while i < len(heaters) - 1 and abs(heaters[i+1] - house) <= abs(heaters[i] - house):
            # the same with the following shorthand
            # notice, must use <= but not <
            while i < len(heaters) - 1 and heaters[i] + heaters[i + 1] <= house * 2:
                i += 1
            min_radius = max(min_radius, abs(heaters[i] - house))
        return min_radius

    def findRadius_binarysearch(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # Time: O(max(mlogn, nlogn))
        # Space: O(1)
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target: left = mid + 1
                else: right = mid - 1
            return left
        heaters.sort()
        min_radius = 0
        for house in houses:
            # find the heaters with the position larger or equal to the position of the house
            index = binary_search(heaters, house)
            left_radius = house - heaters[index - 1] if index > 0 else float('inf')
            right_radius = heaters[index] - house if index < len(heaters) else float('inf')
            min_radius = max(min_radius, min(left_radius, right_radius))
        return min_radius


if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3], [2]), 1),
        (([1, 2, 3, 4], [1, 4]), 1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findRadius(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

