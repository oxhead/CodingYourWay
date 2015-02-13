#!/usr/bin/ruby

=begin
https://www.hackerrank.com/challenges/quicksort3
=end

# Enter your code here. Read input from STDIN. Print output to STDOUT
def partition(ar, low, high)
    pivot_new = low
    i = low
    while i < high
        if ar[i] < ar[high]
            ar[i], ar[pivot_new] = ar[pivot_new], ar[i]
            pivot_new += 1
        end
        i += 1 
    end
    ar[pivot_new], ar[high] = ar[high], ar[pivot_new]
    puts ar.join(" ")
    return pivot_new
end

def quickSort(ar, low, high)
    if low >= high
        return
    end
    
    pivot = partition(ar, low, high)
    quickSort(ar, low, pivot-1)
    quickSort(ar, pivot+1, high) 
end


ar_len = gets.strip.to_i
ar = gets.strip.split(" ").map {|i| i.to_i}
quickSort(ar, 0, ar.size-1)

