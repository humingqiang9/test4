# C++ Project Makefile

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g
INCLUDES = -Iinclude

# Directories
SRCDIR = src
INCDIR = include
TESTDIR = tests
BUILDDIR = build

# Source files
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
OBJECTS = $(SOURCES:$(SRCDIR)/%.cpp=$(BUILDDIR)/%.o)

# Test files
TEST_SOURCES = $(wildcard $(TESTDIR)/*.cpp)
TEST_OBJECTS = $(TEST_SOURCES:$(TESTDIR)/%.cpp=$(BUILDDIR)/%.o)
TEST_TARGETS = $(TEST_SOURCES:$(TESTDIR)/%.cpp=$(BUILDDIR)/%)

# Target executable
TARGET = $(BUILDDIR)/main

# Default target
.PHONY: all
all: build

# Build the main executable
.PHONY: build
build: $(TARGET)

# Link the main executable
$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compile source files
$(BUILDDIR)/%.o: $(SRCDIR)/%.cpp | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Run tests
.PHONY: test
test: $(TEST_TARGETS)
	@echo "Running tests..."
	@for test in $(TEST_TARGETS); do \
		echo "Running $$test..."; \
		./$$test || exit 1; \
	done
	@echo "All tests passed!"

# Compile test executables
$(BUILDDIR)/%: $(TESTDIR)/%.cpp $(filter-out $(BUILDDIR)/main.o, $(OBJECTS)) | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -o $@ $^

# Create build directory
$(BUILDDIR):
	mkdir -p $(BUILDDIR)

# Clean build artifacts
.PHONY: clean
clean:
	rm -rf $(BUILDDIR)