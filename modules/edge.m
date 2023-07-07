// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// This module debounces a boolean signal
// -----------------------------------------------------------------------------

#include "time.h"
#include "Edge.h"

impl Edge
{
    in bool reset;
    in bool input;
    in bool rising;

    var bool on = and(
        rising,
        input,
        not(state)
    );

    var bool off = and(
        not(rising),
        not(input),
        state
    );

    var bool state = and(input,not(reset));

    out bool output = and(
        or(on,off),
        not(reset)
    );
};
