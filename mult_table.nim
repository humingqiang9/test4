import random, strformat

# Procedure to print multiplication table to a file
proc writeMultiplicationTable(filename: string, size: int) =
  let f = open(filename, fmWrite)
  for i in 1..size:
    for j in 1..size:
      f.write(fmt"{i*j:4}")
    f.write("\n")
  f.close()

# Generate a random filename
randomize()
let filename = fmt"mult_table_{rand(10000)}.txt"

# Write the table to the file using the procedure
writeMultiplicationTable(filename, 10)

echo "Multiplication table saved to ", filename