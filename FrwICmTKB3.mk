# Simple Makefile with compile and clean targets

# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c99
TARGET = myprogram
SRCDIR = src
OBJDIR = obj
SOURCES = $(wildcard $(SRCDIR)/*.c)
OBJECTS = $(SOURCES:$(SRCDIR)/%.c=$(OBJDIR)/%.o)

# Default target
all: $(TARGET)

# Create necessary directories
$(OBJDIR):
	mkdir -p $(OBJDIR)

# Compile source files to object files
$(OBJDIR)/%.o: $(SRCDIR)/%.c | $(OBJDIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Link object files to create executable
$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@

# Clean target to remove generated files
clean:
	rm -f $(TARGET)
	rm -rf $(OBJDIR)

# Phony targets
.PHONY: all clean