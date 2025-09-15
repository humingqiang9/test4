# Test the ListReverser module

# Compile the module
Code.compile_file("list_reverser.ex")

# Test cases
IO.puts("Testing ListReverser.reverse/1")

test1 = [1, 2, 3, 4, 5]
result1 = ListReverser.reverse(test1)
IO.inspect(result1, label: "Reverse of #{inspect(test1)}")

test2 = []
result2 = ListReverser.reverse(test2)
IO.inspect(result2, label: "Reverse of #{inspect(test2)}")

test3 = [:a, :b, :c, :d]
result3 = ListReverser.reverse(test3)
IO.inspect(result3, label: "Reverse of #{inspect(test3)}")

test4 = ["hello", "world", 1, 2, 3]
result4 = ListReverser.reverse(test4)
IO.inspect(result4, label: "Reverse of #{inspect(test4)}")