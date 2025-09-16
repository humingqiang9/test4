#include <iostream>
#include <cassert>
#include "utils.h"

void test_square() {
    assert(square(2) == 4);
    assert(square(5) == 25);
    assert(square(-3) == 9);
    std::cout << "All tests passed!" << std::endl;
}

int main() {
    test_square();
    return 0;
}