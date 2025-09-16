# Makefile for C++ project

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g
LDFLAGS = 

# Directories
SRCDIR = src
TESTDIR = test
BUILDDIR = build
BINDIR = bin

# Source files
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
OBJECTS = $(SOURCES:$(SRCDIR)/%.cpp=$(BUILDDIR)/%.o)

# Test files
TEST_SOURCES = $(wildcard $(TESTDIR)/*.cpp)
TEST_OBJECTS = $(TEST_SOURCES:$(TESTDIR)/%.cpp=$(BUILDDIR)/%.o)
TEST_EXECUTABLES = $(TEST_SOURCES:$(TESTDIR)/%.cpp=$(BINDIR)/%)

# Main executable name
TARGET = $(BINDIR)/main

# Default target
all: build

# Build the main executable
build: $(TARGET)

# Create necessary directories
$(BUILDDIR) $(BINDIR):
	mkdir -p $@

# Link the main executable
$(TARGET): $(OBJECTS) | $(BINDIR)
	$(CXX) $(OBJECTS) -o $@ $(LDFLAGS)

# Compile source files
$(BUILDDIR)/%.o: $(SRCDIR)/%.cpp | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Run tests
test: $(TEST_EXECUTABLES)
	@for test_exec in $(TEST_EXECUTABLES); do \
		echo "Running $$test_exec"; \
		$$test_exec || exit 1; \
	done

# Compile test files
$(BINDIR)/%: $(TESTDIR)/%.cpp $(OBJECTS) | $(BINDIR) $(BUILDDIR)
	$(CXX) $(CXXFLAGS) $< $(OBJECTS) -o $@ $(LDFLAGS)

# Clean build artifacts
clean:
	rm -rf $(BUILDDIR) $(BINDIR)

# Phony targets
.PHONY: all build test clean