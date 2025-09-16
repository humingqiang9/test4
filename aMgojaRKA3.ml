(* Функция для проверки четности числа *)
let is_even n =
  n mod 2 = 0

(* Примеры использования *)
let () =
  Printf.printf "2 is even: %b\n" (is_even 2);
  Printf.printf "3 is even: %b\n" (is_even 3);
  Printf.printf "0 is even: %b\n" (is_even 0);
  Printf.printf "-4 is even: %b\n" (is_even (-4));
  Printf.printf "-5 is even: %b\n" (is_even (-5))