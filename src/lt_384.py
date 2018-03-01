"""
https://leetcode.com/problems/shuffle-an-array

Related:

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        index_list = [i for i in range(len(self.nums))]
        for i in range(len(self.nums)):
            j = random.randrange(0, len(index_list))
            index_list[i], index_list[j] = index_list[j], index_list[i]
        return [self.nums[i] for i in index_list]
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle() 

if __name__ == '__main__':
    test_cases = [
    ]

    records = set()
    obj = Solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    for _ in range(10):
        output = tuple(obj.shuffle())
        print('shuffle:', output)
        if output in records:
            assert False
        records.add(output)
