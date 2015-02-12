#!/usr/bin/ruby

require 'set'

sentence = gets.chomp.downcase
record = Set.new
sentence.each_char {|x| record.add(x) if (x >= 'a' and x <= 'z') }
print record.size() == 26 ? "pangram" : "not pangram"
