"""
http://www.lintcode.com/en/problem/sort-colors-ii

Related:
  - lt_74

Complexity:
  - Time:
  - Space:
"""

"""
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Notice
You are not suppose to use the library's sort function for this problem.
k <= n

Example
Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?

"""

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        left, right = 0, len(colors) - 1
        left_color, right_color = 1, k
        index = 0
        while left_color < right_color:
            while index <= right:
                if colors[index] == left_color:
                    colors[index], colors[left] = colors[left], colors[index]
                    index += 1
                    left += 1
                elif colors[index] == right_color:
                    colors[index], colors[right] = colors[right], colors[index]
                    right -= 1
                else:
                    index += 1
            index = left
            left_color += 1
            right_color -= 1
           

    def sortColors2_twopass(self, colors, k):
        counter = [0] * k
        for color in colors:
            counter[color - 1] += 1
        index = 0
        for color, color_count in enumerate(counter):
            for _ in range(color_count):
                colors[index] = color + 1
                index += 1
                

if __name__ == '__main__':
    test_cases = [
        (([3, 2, 2, 1, 4], 4), [1, 2, 2, 3, 4]),
        (([2, 1, 1, 2, 2], 2), [1, 1, 2, 2, 2]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        nums, k = test_case[0]
        Solution().sortColors2(nums, k)
        print('output:', nums)
        assert nums == test_case[1]

