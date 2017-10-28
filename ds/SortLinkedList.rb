#!/usr/bin/ruby

=begin
=end

load "LinkedList.rb"

def sort(list)
  return if not list

  current = list.head._next
  while current
    # remember the next node to start with
    next_current = current._next
    forward = current._previous
    while forward
      if current.value < forward.value
        current._next._previous = forward if current._next
        forward._previous._next = current if forward._previous

        # case 1: swap two nodes next to each other
        # case 2: otherwise
        if current._previous == forward
            temp_current_next = current._next
            current._next = forward
            current._previous = forward._previous
            forward._next = temp_current_next
            forward._previous = current
        else
            temp_current_next = current._next
            temp_current_previous = current._previous
            current._next = forward._next
            current._previous = forward._previous
            forward._next = temp_current_next
            forward._previous = temp_current_previous
        end

        
        # check head pointer
        list.head = current if forward == list.head
        forward = current._previous
      else
        break 
      end
    end
    current = next_current
  end
end


if $0 == __FILE__

  n = rand(20..20)
  previous = nil
  list = LinkedList.new nil
  (1..n).each do |i|
    node = DNode.new rand(1..100)
    list.head = node if not list.head
    previous._next = node if previous
    node._previous = previous
    previous = node
  end

  puts 'before'
  print_list list.head
  sort(list)
  puts 'after'
  print_list list.head
  puts ''
end
