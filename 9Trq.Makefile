# Simple Makefile for compiling a C program

# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall -Wextra -std=c99

# Target executable name
TARGET = program

# Default rule
all: $(TARGET)

# Rule to compile the C program
$(TARGET): main.c
	$(CC) $(CFLAGS) -o $(TARGET) main.c

# Clean rule to remove compiled files
clean:
	rm -f $(TARGET)

# Install rule (placeholder)
install:
	@echo "Installing $(TARGET) to /usr/local/bin"
	# sudo cp $(TARGET) /usr/local/bin/

.PHONY: all clean install