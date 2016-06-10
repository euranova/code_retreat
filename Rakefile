require "rake"

def print_line
  puts "-" * 80
end

def print_header(title)
  print_line
  puts title
  print_line
end

task :bash do
  print_header("Ruby")
  puts `cd scaffolds/bash; bats test`
  print_line
end

task :ruby do
  print_header("Bash")
  puts `cd scaffolds/ruby; rake`
  print_line
end

task all: [
  :bash,
  :ruby
]
task default: :all
