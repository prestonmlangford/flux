// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// Pulse train for a given period.
// -----------------------------------------------------------------------------
#ifndef CLOCK_H
#define CLOCK_H

decl Clock
{
    const u64 TICKS_PER_NS;
    const u64 TICKS_PER_US;
    const u64 TICKS_PER_MS;

    in boolean reset;
    in u64 period_in_ticks;
    out boolean signal;
};

#endif // CLOCK_H 

