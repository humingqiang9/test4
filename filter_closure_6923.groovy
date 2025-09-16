// Groovy script demonstrating a closure for filtering lists

// Define a list of numbers
def numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Create a closure that filters even numbers
def evenFilter = { it % 2 == 0 }

// Apply the filter closure to the list
def evenNumbers = numbers.findAll(evenFilter)

// Print the results
println "Original list: $numbers"
println "Filtered list (even numbers): $evenNumbers"

// Another example with strings
def words = ["apple", "banana", "cherry", "date", "elderberry"]

// Closure to filter words longer than 5 characters
def longWordFilter = { it.length() > 5 }

def longWords = words.findAll(longWordFilter)

println "\nOriginal words: $words"
println "Filtered words (longer than 5 chars): $longWords"
