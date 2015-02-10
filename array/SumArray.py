#!/usr/bin/py
# -*- coding: utf-8 -*-

'''
SumArray, https://www.hackerrank.com/challenges/solve-me-second

Problem Statement
The task is to scan two numbers from STDIN, and print the sum A+B on STDOUT. The code has already been provided for most of the popular languages. This is primarily for you to read and inspect how the IO is handled.

Input Format 
This section specifies the Input Format. 
The first line contains T (number of test cases) followed by T lines 
Each line contains A and B separated by a space.

Output Format 
This section specifies the Output Format. 
An integer that denotes Sum (A+B) printed on new line for every testcase.

Constraints 
This section tells what input you can expect. You can freely assume that the input will remain within the boundaries specified. As an example here given below, A and B will never be below 1 or above 1000. 
1≤T≤1000 
1≤A,B≤1000

'''

if __name__ == '__main__':
    num_line = int(raw_input())
    for i in range(num_line):
        print sum(map(int, raw_input().strip().split(' ')))
