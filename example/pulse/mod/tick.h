// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// A custom module for a monotonic clock
// -----------------------------------------------------------------------------
#ifndef TICK_H
#define TICK_H

decl Tick
{
    in boolean reset;
    out u64 ticks;
};

#endif // TICK_H
