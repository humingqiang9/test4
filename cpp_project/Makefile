# Makefile for C++ Project

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g
INCLUDES = -Iinclude

# Directories
SRC_DIR = src
INC_DIR = include
BUILD_DIR = build

# Source files (excluding test files)
SRCS = $(filter-out $(SRC_DIR)/test_main.cpp, $(wildcard $(SRC_DIR)/*.cpp))
OBJS = $(SRCS:$(SRC_DIR)/%.cpp=$(BUILD_DIR)/%.o)

# Test files
TEST_SRCS = $(SRC_DIR)/test_main.cpp
TEST_OBJS = $(TEST_SRCS:$(SRC_DIR)/%.cpp=$(BUILD_DIR)/%.o)
TEST_TARGET = $(BUILD_DIR)/test_runner

# Main executable target
TARGET = $(BUILD_DIR)/main

# Default target
all: $(TARGET)

# Create build directory if it doesn't exist
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Link object files to create main executable
$(TARGET): $(OBJS) | $(BUILD_DIR)
	$(CXX) $(OBJS) -o $@

# Link object files to create test executable
$(TEST_TARGET): $(filter-out $(BUILD_DIR)/main.o, $(OBJS)) $(TEST_OBJS) | $(BUILD_DIR)
	$(CXX) $(filter-out $(BUILD_DIR)/main.o, $(OBJS)) $(TEST_OBJS) -o $@

# Compile source files to object files
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp | $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Build and run tests
test: $(TEST_TARGET)
	@echo "Running tests..."
	./$(TEST_TARGET)
	@echo "Tests completed."

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)

# Clean all including test outputs
clean-all: clean
	rm -f test_output.txt

.PHONY: all test clean clean-all