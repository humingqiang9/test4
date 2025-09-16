#include <iostream>
#include <algorithm>
#include <vector>

void printArray(const std::vector<int>& arr) {
    for (size_t i = 0; i < arr.size(); ++i) {
        std::cout << arr[i];
        if (i < arr.size() - 1) {
            std::cout << " ";
        }
    }
    std::cout << std::endl;
}

int main() {
    // Initialize an array with some integers
    std::vector<int> numbers = {64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42};
    
    std::cout << "Original array: ";
    printArray(numbers);
    
    // Sort the array in ascending order
    std::sort(numbers.begin(), numbers.end());
    
    std::cout << "Sorted array: ";
    printArray(numbers);
    
    return 0;
}