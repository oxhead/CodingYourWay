#!/usr/bin/ruby
def  insertionSort(ar) 
    0.upto(ar.size - 2) do |i|
        j = i + 1
        while (j > 0) do
            if ar[j] < ar[j-1]
                ar[j], ar[j-1] = ar[j-1], ar[j]
            end
            j -= 1
        end
        print "%s\n" % ar.join(" ")
    end
end
cnt = gets.to_i
ar = gets.strip.split(" ").map! {|i| i.to_i}
insertionSort(ar)

