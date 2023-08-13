SHELL := bash
ROOT := $(PWD)
BLD := $(ROOT)/build
SRC := $(ROOT)/src
COV := $(ROOT)/coverage
OUT := bin
CC := export CC="gcc"; export CPP="gcc -E"; python -m acc
# CC := gcc
LD := ld
INC := -I../libasync
OBJ = $(call rwildcard,$(BLD),*.o)

CFLAGS =
# CFLAGS += -fprofile-arcs
# CFLAGS += -ftest-coverage
# CFLAGS += -nostdlib
CFLAGS += -g
CFLAGS += -Wall

LDFLAGS :=
LDFLAGS += -lasync
LDFLAGS += -L../libasync

# utility macros
getdir=$(dir $(filter %/$(strip $(1)).mk, $(MAKEFILE_LIST)))
objects=$(patsubst %.c,$(BLD)/$(subst $(SRC)/,,$(call getdir, $(1)))%.o,$(2))
rwildcard=$(foreach d,$(wildcard $(1:=/*)),$(call rwildcard,$d,$2) $(filter $(subst *,%,$2),$d))

include $(call rwildcard,$(SRC),*.mk)

bin: main
	@$(CC) $(OBJ) -o $(OUT) $(LDFLAGS)

all: build main

$(BLD)/%.o: $(SRC)/%.c
	@$(CC) -c -o $@ $< $(CFLAGS) $(INC)

run:
	@$(ROOT)/$(OUT)

clean:
	@rm -f $(OUT)
	@rm -rf $(BLD)
	@rm -rf $(COV)
	@rm -f *.zip
	@INCLUDE=

build: clean
	@cd $(SRC); rsync -a --include='*/' --exclude='*' . $(BLD)

.PHONY: all test clean coverage
