#!/usr/bin/ruby

load "../data_structure/Stack.rb"

=begin
https://www.hackerrank.com/challenges/quicksort3
=end

class Disk
    attr_accessor :id
    def initialize(id)
        @id = id
    end
end

class Tower < Stack
    attr_accessor :id
    def initialize(id)
        @id = id
    end

    def move_disks(n, tower_to, tower_temp)
        if n > 0
          move_disks(n-1, tower_temp, tower_to)
          move_top(tower_to)
          tower_temp.move_disks(n-1, tower_to, self)
        end
        
    end
    def move_top(tower_to)
        disk = pop
        tower_to.push(disk)
        puts "Move disk #{disk.id} from tower #{self.id} to tower #{tower_to.id}"
    end
end

def solve(num_disks)
    towers = []
    (1..3).each do |i|
        towers.push(Tower.new(i))
    end
    num_disks.downto(1).each do |i|
        towers[0].push(Disk.new(i))
    end
    towers[0].move_disks(num_disks, towers[2], towers[1])
end

num_disks = gets.strip.to_i
solve(num_disks)
