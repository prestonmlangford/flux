// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// This module processes the landing indications
// -----------------------------------------------------------------------------

#include "time.h"

#include "edge.h"
// decl module Edge
// {
//     in bool reset;
//     in bool input;
//     in bool rising;
//     out bool output;
// };


#include "debounce.h"
// decl module Debounce
// {
//     in bool reset;
//     in bool input;
//     in bool rising;
//     out bool output;
// };

const i32 LANDING_ALTITUDE = i32(100);

module Landing
{
    in i32 fuel;
    in bool wow;
    in bool flight;

    state Coordinates coor = {
        .now = bool(1)
    };

    state Debounce db = {
        .input = wow,
        .duration = i64(123)
    };

    state Edge edge = {
        .input = db.result,
        .rising = bool(0)
    };

    state bool transit = not(flight);
    state f64 larpitude[2] = sum(coor.latitude, 
                               coor.longitude);

    out bool stop = db.result;
    out bool start = and(db.output,edge.output,transit);
};
