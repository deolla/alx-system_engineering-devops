#!/usr/bin/env ruby
# create a Ruby script that accepts one argument and pass it
# to a regular expression matching method.

put ARGV[0].scan(/hbt{2,4)n/).join
