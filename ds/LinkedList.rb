#!/usr/bin/ruby

=begin
https://www.hackerrank.com/challenges/icecream-parlor
=end

class Node
  attr_accessor :value, :_next
  def initialize(value=nil, _next=nil)
    @value = value
    @_next = _next
  end
end

class DNode < Node
  attr_accessor :_previous
  def initialize(value=nil, _next=nil, _previous=nil)
    super(value, _next)
    @_previous = _previous
  end
end

class LinkedList
  attr_accessor :head
  def initialize(head)
    @head = head
  end
end

def print_list(node)
  current = node
  while current
    current._next ? (print "%s, " % current.value) : (print current.value)
    current = current._next
  end
  puts ''
end
