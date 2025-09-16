(* Recursive factorial function in OCaml *)
let rec factorial n =
  if n <= 1 then 1
  else n * factorial (n - 1)

(* Test the function *)
let () =
  print_string "Factorial of 5 is: ";
  print_int (factorial 5);
  print_newline ();
  
  print_string "Factorial of 10 is: ";
  print_int (factorial 10);
  print_newline ()