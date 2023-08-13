// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// Pulse train for a given period.
// -----------------------------------------------------------------------------
#ifndef CLOCK_H
#define CLOCK_H

decl Clock
{
    in boolean reset;
    in u64 period_ns;
    out boolean output;
};

#endif // CLOCK_H 

