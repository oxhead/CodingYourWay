#!/usr/bin/py
# -*- coding: utf-8 -*-

'''
Lonely Integer, https://www.hackerrank.com/challenges/lonely-integer

Problem Statement
There are N integers in an array A. All but one integer occur in pairs. Your task is to find out the number that occurs only once.

Input Format
The first line of the input contains an integer N indicating the number of integers. 
The next line contains N space separated integers that form the array A.

Constraints
1 <= N < 100 
N % 2 = 1 ( N is an odd number ) 
0 <= A[i] <= 100, ∀ i ∈ [1, N]

Output Format
Output S, the number that occurs only once.
'''

def lonelyinteger(array):
    record = set()
    for n in array:
        record.remove(n) if n in record else record.add(n)
    answer = list(record)[0]
    return answer

if __name__ == '__main__':
    array_len = int(input())
    array = map(int, raw_input().strip().split(" "))
    print(lonelyinteger(array))

