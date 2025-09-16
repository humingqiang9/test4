import random, strformat, os

proc generateMultiplicationTable(size: int): string =
  result = ""
  for i in 1..size:
    for j in 1..size:
      result &= fmt"{i*j:3} "
    result &= "\n"

proc main() =
  # Generate a random filename
  randomize()
  let filename = "mult_table_" & $rand(1000..9999) & ".txt"
  
  # Generate the table
  let table = generateMultiplicationTable(9)
  
  # Write to file
  writeFile(filename, table)
  
  echo "Table saved to ", filename

main()