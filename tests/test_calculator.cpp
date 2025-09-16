#include <iostream>
#include <cassert>
#include "calculator.h"

int main() {
    // Test add function
    assert(Calculator::add(2, 3) == 5);
    assert(Calculator::add(-1, 1) == 0);
    assert(Calculator::add(0, 0) == 0);
    
    // Test multiply function
    assert(Calculator::multiply(3, 4) == 12);
    assert(Calculator::multiply(-2, 3) == -6);
    assert(Calculator::multiply(0, 5) == 0);
    
    std::cout << "All tests passed!" << std::endl;
    return 0;
}