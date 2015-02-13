#!/usr/bin/ruby

=begin
https://www.hackerrank.com/challenges/circle-city
=end

def check(r, k)
    count = 0
    (0..(Math.sqrt(r).to_i-1)).each do |i|
        j = Math.sqrt(r-i*i)
        count += 1 if (j.to_i == j.ceil)
        puts "i=%s, j=%s, %s, %s, %s" % [i, j, j.to_i, j.ceil, j.to_i == j.ceil]
    end
    count = count * 4
    puts count <= k ? "possible" : "impossible"
end

t = gets.strip.to_i
(1..t).each do |t|
    testcase = gets.strip.split(" ").map {|i| i.to_i}
    r, k = testcase
    check(r, k)
end
