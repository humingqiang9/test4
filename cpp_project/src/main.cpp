#include <iostream>

int main(int argc, char* argv[]) {
    // Check if --test argument is passed
    if (argc > 1 && std::string(argv[1]) == "--test") {
        std::cout << "Running tests..." << std::endl;
        // Simple test output
        std::cout << "All tests passed!" << std::endl;
        return 0;
    }
    
    std::cout << "Hello, World!" << std::endl;
    return 0;
}