#!/usr/bin/ruby

=begin
https://www.hackerrank.com/challenges/insertionsort1
=end

def  insertionSort(ar) 
    n_index = ar.size - 1
    n = ar[n_index]
    (ar.size-1).downto(0) do |i|
        sorted = false
        if i < 1
            ar[i] = n
        elsif ar[i-1] > n
            ar[i] = ar[i-1]
        else
            ar[i] = n 
            sorted = true
        end
        print "%s\n" % ar.join(" ")
        break if sorted
    end

end

count = gets.to_i
ar = gets.strip.split.map {|i| i.to_i}

insertionSort( ar )
