'''
https://oj.leetcode.com/problems/two-sum/
'''

def Sum(num, target):
	record = {}
	for i in range(len(num)):
		if num[i] in record:
			return (record[num[i]], i)
                else:
			record[target-num[i]] = i
			print record
	return (-1, -1)

print Sum([3, 2, 4], 6)
