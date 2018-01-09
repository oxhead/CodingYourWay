"""
https://leetcode.com/problems/fizz-buzz/

Related
"""

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output "Fizz" instead of the number and for the multiples of five output "Buzz". For numbers which are multiples of both three and five output "FizzBuzz".

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]


"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1, n+1):
            if i % 15 == 0: output.append("FizzBuzz")
            elif i % 3 == 0: output.append("Fizz")
            elif i % 5 == 0: output.append("Buzz")
            else: output.append(str(i))
        return output

if __name__ == '__main__':
    test_cases = [
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().fizzBuzz(test_case[0])
        print('output:', output)
        assert output == test_case[1]

