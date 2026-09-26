#!/usr/bin/env ruby

numbers = ARGV.select { |arg| arg =~ /\A-?\d+\z/ }.map(&:to_i)
numbers.sort.each { |n| puts n }
