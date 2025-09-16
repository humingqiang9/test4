#include <iostream>
#include "../include/utils.h"

int main() {
    int result = square(4);
    if (result == 16) {
        std::cout << "Test passed: square(4) = " << result << std::endl;
        return 0;
    } else {
        std::cout << "Test failed: square(4) = " << result << std::endl;
        return 1;
    }
}