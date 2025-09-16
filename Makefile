# Makefile for C++ project

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -g
INCLUDES = -Iinclude

# Directories
SRCDIR = src
TESTDIR = tests
BUILDDIR = build
TARGET = $(BUILDDIR)/main
TESTTARGET = $(BUILDDIR)/test

# Source files
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
TESTSOURCES = $(TESTDIR)/test_calculator.cpp
OBJECTS = $(SOURCES:$(SRCDIR)/%.cpp=$(BUILDDIR)/%.o)
TESTOBJECTS = $(filter-out $(BUILDDIR)/main.o, $(OBJECTS)) $(BUILDDIR)/test_calculator.o

# Default target
all: $(TARGET)

# Create build directory
$(BUILDDIR):
	mkdir -p $(BUILDDIR)

# Build the main executable
$(TARGET): $(OBJECTS) | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compile source files
$(BUILDDIR)/%.o: $(SRCDIR)/%.cpp | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Build and run tests
test: $(TESTTARGET)
	./$(TESTTARGET)

# Build test executable
$(TESTTARGET): $(TESTOBJECTS) $(BUILDDIR)/test_calculator.o | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compile test files
$(BUILDDIR)/test_calculator.o: $(TESTSOURCES) | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Clean build artifacts
clean:
	rm -rf $(BUILDDIR)

# Phony targets
.PHONY: all test clean