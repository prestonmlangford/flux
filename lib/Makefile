SHELL := bash
ROOT := $(PWD)
OBJ := $(ROOT)/obj
SRC := $(ROOT)/ops
OUT := libflux.a
CC := gcc

# utility functions
skeleton=cd $(1); rsync -a --include='*/' --exclude='*' . $(2)
transmove = $(subst $(1),$(2),$(patsubst %.$(3),%.$(4) ,$(wildcard $(1)/*.$(3))))


INC := -I$(ROOT) -I$(SRC)
SRCS := $(wildcard $(SRC)/*.c)
OBJS := $(subst $(SRC),$(OBJ),$(patsubst %.c,%.o,$(SRCS)))

CFLAGS =
# CFLAGS += -fprofile-arcs
# CFLAGS += -ftest-coverage
# CFLAGS += -nostdlib
# CFLAGS += -g
CFLAGS += -Wall

obj_dir:
	@$(call skeleton,$(SRC),$(OBJ))

obj: obj_dir $(OBJS)

$(OUT): $(OBJS)
	@ar cr $@ $+

lib: obj $(OUT)

$(OBJ)/%.o: $(SRC)/%.c
	@$(CC) $(INC) -c -o $@ $< $(CFLAGS)

clean:
	@rm -f $(OUT)
	@rm -rf $(OBJ)

.PHONY: all test clean coverage
