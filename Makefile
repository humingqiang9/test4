# Makefile for C++ project

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g
LDLIBS = -lm

# Directories
SRCDIR = src
TESTDIR = tests
BUILDDIR = build
TARGET = app
TESTTARGET = test_runner

# Source files
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
OBJECTS = $(SOURCES:$(SRCDIR)/%.cpp=$(BUILDDIR)/%.o)

# Test files
TEST_SOURCES = $(wildcard $(TESTDIR)/*.cpp)
TEST_OBJECTS = $(TEST_SOURCES:$(TESTDIR)/%.cpp=$(BUILDDIR)/%.o)

# Default target
all: build

# Build the main application
build: $(BUILDDIR) $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDLIBS)

# Build the test executable
test: $(BUILDDIR) $(TESTTARGET)

$(TESTTARGET): $(OBJECTS) $(TEST_OBJECTS)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDLIBS)

# Create build directory
$(BUILDDIR):
	mkdir -p $(BUILDDIR)

# Compile source files
$(BUILDDIR)/%.o: $(SRCDIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Compile test files
$(BUILDDIR)/%.o: $(TESTDIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Clean build artifacts
clean:
	rm -rf $(BUILDDIR) $(TARGET) $(TESTTARGET)

# Run tests
run-test: test
	./$(TESTTARGET)

.PHONY: all build test clean run-test