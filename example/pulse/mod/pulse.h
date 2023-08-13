// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// Boolean periodic pulse train
// -----------------------------------------------------------------------------
#ifndef PULSE_H
#define PULSE_H

decl Pulse
{
    in boolean reset;
    in u64 period_ns;
    out boolean output;
};

#endif // PULSE_H 
