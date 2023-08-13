// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// This module debounces a boolean signal
// -----------------------------------------------------------------------------

#include "time.h"
#include "debounce.h"

module Debounce
{
    in bool reset;
    in bool input;
    in i64 duration;

    state i64 now = time();
    state bool unstable = or(reset,xor(input,state));
    state i64 before = mux(unstable,now,before);

    state i64 elapsed = sub(now,before);
    state bool expired = gt(elapsed,duration);

    state bool state = and(
        not(reset),
        mux(expired,input,state)
    );

    out bool output = state;
};