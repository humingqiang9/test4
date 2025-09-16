// Замыкание для фильтрации четных чисел из списка
def filterEvenNumbers = { list ->
    return list.findAll { it % 2 == 0 }
}

// Пример использования
def numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def evenNumbers = filterEvenNumbers(numbers)

println "Исходный список: ${numbers}"
println "Отфильтрованный список (четные числа): ${evenNumbers}"

// Еще одно замыкание для фильтрации строк по длине
def filterByLength = { list, minLength ->
    return list.findAll { it.length() >= minLength }
}

// Пример использования второго замыкания
def words = ["Groovy", "_closure", "filter", "list", "programming"]
def longWords = filterByLength(words, 6)

println "\nИсходный список строк: ${words}"
println "Отфильтрованный список (строки длиной 6+ символов): ${longWords}"