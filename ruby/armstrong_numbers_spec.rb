# The code is written as driver code. Can you convert it to RSPEC?

require_relative 'armstrong_numbers'

puts find_armstrong_numbers([0]) == [0]
puts find_armstrong_numbers([*0..7]) == [0, 1, 2, 3, 4, 5, 6, 7]
puts find_armstrong_numbers([*0..99]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
puts find_armstrong_numbers([*0..999]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
