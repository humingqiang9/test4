#include <iostream>
#include "calculator.h"

int main() {
    Calculator calc;
    
    // Test addition
    int result1 = calc.add(2, 3);
    if (result1 == 5) {
        std::cout << "Addition test passed!" << std::endl;
    } else {
        std::cout << "Addition test failed!" << std::endl;
        return 1;
    }
    
    // Test multiplication
    int result2 = calc.multiply(2, 3);
    if (result2 == 6) {
        std::cout << "Multiplication test passed!" << std::endl;
    } else {
        std::cout << "Multiplication test failed!" << std::endl;
        return 1;
    }
    
    return 0;
}