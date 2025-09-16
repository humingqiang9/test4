#include <iostream>
#include "calculator.h"

int main() {
    int result = Calculator::add(5, 3);
    std::cout << "5 + 3 = " << result << std::endl;
    
    result = Calculator::multiply(4, 6);
    std::cout << "4 * 6 = " << result << std::endl;
    
    return 0;
}