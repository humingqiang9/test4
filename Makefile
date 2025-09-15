# Makefile for C++ project

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -g
INCLUDES = -Iinclude

# Directories
SRCDIR = src
TESTDIR = tests
BUILDDIR = build

# Source files
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
TEST_SOURCES = $(TESTDIR)/test_calculator.cpp

# Object files
OBJECTS = $(SOURCES:$(SRCDIR)/%.cpp=$(BUILDDIR)/%.o)
TEST_OBJECTS = $(TEST_SOURCES:$(TESTDIR)/%.cpp=$(BUILDDIR)/%.o)

# Executables
TARGET = $(BUILDDIR)/main
TEST_TARGET = $(BUILDDIR)/test_calculator

# Default target
all: $(TARGET)

# Build the main executable
$(TARGET): $(OBJECTS) | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Build object files
$(BUILDDIR)/%.o: $(SRCDIR)/%.cpp | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Create build directory
$(BUILDDIR):
	mkdir -p $(BUILDDIR)

# Build and run tests
test: $(TEST_TARGET)
	./$(TEST_TARGET)

# Build test executable
$(TEST_TARGET): $(filter-out $(BUILDDIR)/main.o, $(OBJECTS)) $(TEST_OBJECTS) | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -o $@ $^

# Build test object files
$(BUILDDIR)/%.o: $(TESTDIR)/%.cpp | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Clean build files
clean:
	rm -rf $(BUILDDIR)

# Phony targets
.PHONY: all clean test