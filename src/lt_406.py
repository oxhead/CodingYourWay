"""
https://leetcode.com/problems/queue-reconstruction-by-height

Related:
  - lt_315_count-of-smaller-numbers-after-self
"""

"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Time: O(n^2)
        # Space: O(1)
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            # if the index is larger than current size, put it at the end.
            output.insert(p[1], p)
        return output

    def reconstructQueue_failed(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        output = [people[0]]
        for p in people[1:]:
            index = 0
            count = p[1]
            while index < len(output):
                if p[1] == 0 and p[0] < output[index][0]: break
                if p[0] <= output[index][0] and count >= 0:
                    count -= 1
                index += 1
            output.insert(index, p)
        return output


if __name__ == '__main__':
    test_cases = [
       ([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]], [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]), 
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().reconstructQueue(test_case[0])
        print('output:', output)
        assert output == test_case[1]
