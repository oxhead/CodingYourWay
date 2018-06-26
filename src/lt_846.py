"""
https://leetcode.com/contest/weekly-contest-87/problems/hand-of-straights/
"""

"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

 

Note:

    1 <= hand.length <= 10000
    0 <= hand[i] <= 10^9
    1 <= W <= hand.length
"""

class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if not hand: return False
        elif len(hand) % W != 0: return False

        hand.sort()
        while hand:
            start = hand[0]
            indexs = [0]
            for i in range(1, len(hand)):
                if len(indexs) == W: break
                if hand[i] == hand[indexs[len(indexs) - 1]] + 1:
                    indexs.append(i)
            if len(indexs) != W: return False
            for i in reversed(indexs):
                del hand[i]
        return True
        

if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3], 1), True),
        (([1,2,3,6,2,3,4,7,8], 3), True),
        (([1,2,3,4,5], 4), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().isNStraightHand(*test_case[0])
        print('output:', output)
        assert output == test_case[1]
