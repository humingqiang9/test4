#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    // Initialize an array of integers
    std::vector<int> numbers = {64, 34, 25, 12, 22, 11, 90, 5};
    
    // Print the original array
    std::cout << "Original array: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // Sort the array in ascending order
    std::sort(numbers.begin(), numbers.end());
    
    // Print the sorted array
    std::cout << "Sorted array: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
}