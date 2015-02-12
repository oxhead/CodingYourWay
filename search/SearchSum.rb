#!/usr/bin/ruby

=begin
https://www.hackerrank.com/challenges/icecream-parlor
=end

T = gets.to_i
(1..T).each do |x|
    amount = gets.to_i
    flavors = gets.to_i
    arr = gets.strip.split(' ').map! {|x| x.to_i}
    index1 = 0
    index2 = 0
    found = false
    while ((index1 < arr.size()) && !found)
        index2 = index1 + 1
        while index2 < arr.size() and not found
            if (arr[index1] + arr[index2]) == amount
                found = true
            end
            index2 = index2 + 1
        end
        index1 = index1 + 1
    end
    puts "%s %s" % [index1, index2]
end
