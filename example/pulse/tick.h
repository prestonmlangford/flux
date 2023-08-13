// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// A custom module for a monotonic clock
// -----------------------------------------------------------------------------
#ifndef TICK_H
#define TICK_H

#include "flux.h"

struct Tick
{
    boolean reset;
    u64 start;
    u64 ticks;
};

void module_tick(struct Tick* self);

#endif // TICK_H
