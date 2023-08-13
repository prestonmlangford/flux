SHELL := bash
FLUX := ../..
ROOT := $(PWD)
OBJ := $(ROOT)/obj
MOD := $(ROOT)/mod
SRC := $(ROOT)/src
COV := $(ROOT)/coverage
OUT := bin
CPP := gcc -E -P
CC := gcc
FC := python $(FLUX)/lang/main.py
LD := ld
INC := -I$(FLUX)/lib -I$(ROOT) -I$(SRC)
MODS := $(wildcard $(MOD)/*.m)
SRCS := $(subst $(MOD),$(SRC),$(patsubst %.m,%.c,$(MODS)))
OBJS := $(subst $(SRC),$(OBJ),$(patsubst %.c,%.o,$(SRCS)))

# utility functions
skeleton=cd $(1); rsync -a --include='*/' --exclude='*' . $(2)

CFLAGS =
# CFLAGS += -fprofile-arcs
# CFLAGS += -ftest-coverage
# CFLAGS += -nostdlib
CFLAGS += -g
CFLAGS += -Wall

LDFLAGS :=
LDFLAGS += -lflux
LDFLAGS += -L$(FLUX)/lib

bin: $(OBJ)
	@$(CC) tick.c main.c $(OBJS) -o $(OUT) $(LDFLAGS) $(CFLAGS) $(INC)

all: src obj bin

src_dir:
	@$(call skeleton,$(MOD),$(SRC))

src: src_dir $(SRCS)

obj_dir:
	@$(call skeleton,$(SRC),$(OBJ))

obj: obj_dir $(OBJS)

$(OBJ)/%.o: $(SRC)/%.c
	@$(CC) -c -o $@ $< $(CFLAGS) $(INC)

$(SRC)/%.c: $(MOD)/%.m
	@echo "Makefile rule $@ $<"
	@$(CPP) -c -o tmp $< $(CFLAGS) $(INC)
	@$(FC) tmp $@
	@ rm tmp

clean:
	@rm -f $(OUT)
	@rm -rf $(OBJ)
	@rm -rf $(SRC)


dbg: FORCE
	@echo $(MODS)

FORCE: ;
.PHONY: all test clean coverage
