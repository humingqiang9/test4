#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

int main() {
    // Пример массива целых чисел
    std::vector<int> arr = {3, 5, 7, 2, 8, -1, 4, 10, 12};
    
    // Проверка на пустой массив
    if (arr.empty()) {
        std::cout << "Массив пуст." << std::endl;
        return 0;
    }
    
    // Нахождение максимального элемента
    int max_element = *std::max_element(arr.begin(), arr.end());
    
    // Альтернативный способ без использования std::max_element
    // int max_element = INT_MIN;
    // for (int num : arr) {
    //     if (num > max_element) {
    //         max_element = num;
    //     }
    // }
    
    std::cout << "Максимальный элемент в массиве: " << max_element << std::endl;
    
    return 0;
}