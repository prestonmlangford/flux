// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// Detects edges on a boolean signal
// -----------------------------------------------------------------------------

#include "edge.h"

impl Edge
{
    in boolean reset;
    in boolean rising;
    in boolean input;

    var boolean on = and(
        rising,
        input,
        not(state)
    );

    var boolean off = and(
        not(rising),
        not(input),
        state
    );

    var boolean state = and(input,not(reset));

    out boolean output = and(
        or(on,off),
        not(reset)
    );
};