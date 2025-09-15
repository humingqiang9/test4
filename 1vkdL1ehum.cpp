#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <ctime>

int main() {
    // Create a random number generator
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(1, 100);
    
    // Generate a random array size between 5 and 15
    int arraySize = dis(gen) % 11 + 5;
    
    // Create vector with random size
    std::vector<int> numbers(arraySize);
    
    // Fill the vector with random numbers
    std::cout << "Generated array: ";
    for (int i = 0; i < arraySize; ++i) {
        numbers[i] = dis(gen);
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;
    
    // Find maximum element using std::max_element
    auto maxElement = std::max_element(numbers.begin(), numbers.end());
    
    // Print the maximum element
    std::cout << "Maximum element: " << *maxElement << std::endl;
    
    return 0;
}