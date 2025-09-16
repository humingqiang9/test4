# Simple Makefile for Erlang gen_server example

MODULES = simple_counter
ERL_SOURCES = $(MODULES:=.erl)
ERL_OBJECTS = $(MODULES:=.beam)

.PHONY: all clean

all: $(ERL_OBJECTS)

%.beam: %.erl
	erlc $<

clean:
	rm -f *.beam