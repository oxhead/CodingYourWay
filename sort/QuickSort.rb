#!/usr/bin/ruby

=begin
https://www.hackerrank.com/challenges/quicksort2
=end

def quickSort(ar)
    if ar.size <= 1
        return ar
    else
        list1 = []
        list2 = []
        pivot = ar[0]
        (1..ar.size-1).each do |i|
            ar[i] < pivot ? list1.push(ar[i]) : list2.push(ar[i])
        end
        list = quickSort(list1) + [pivot] + quickSort(list2)
        print "%s\n" % list.join(" ")
        return list
    end

end
cnt = gets.to_i;
ar = STDIN.gets.chomp.split(" ").map {|i| i.to_i};
quickSort(ar);


