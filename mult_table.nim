import random

# Procedure to print multiplication table
proc printMultiplicationTable(size: int) =
  for i in 1..size:
    for j in 1..size:
      stdout.write($(i * j) & "\t")
    stdout.write("\n")

# Print the table
printMultiplicationTable(10)