"""
https://leetcode.com/problems/tenth-line

Related:
"""

"""
How would you print just the 10th line of a file?

For example, assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

Your script should output the tenth line, which is:

Line 10

[show hint]
Hint:
1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities. 
"""

# https://github.com/kamyu104/LeetCode/blob/master/Shell/tenth-line.sh

# Read from the file file.txt and output all valid phone numbers to stdout.

# Solution 1
# awk '{if(NR==10) print $0}' file.txt
# awk 'NR == 10' file.txt

# Solution 2
# sed -n 10p file.txt

# Solution 3
tail -n+10 file.txt | head -1
