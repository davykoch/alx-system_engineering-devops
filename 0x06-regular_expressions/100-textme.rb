#!/usr/bin/env ruby

log_line = ARGV[0]

# Extracting sender, receiver, and flags using regular expressions
sender = log_line.scan(/\[from:([\w\+\-\(\)]+)\]/).flatten.first
receiver = log_line.scan(/\[to:([\w\+\-\(\)]+)\]/).flatten.first
flags = log_line.scan(/\[flags:([^\]]+)\]/).flatten.first

# Output the result in the specified format
puts "#{sender},#{receiver},#{flags}"
