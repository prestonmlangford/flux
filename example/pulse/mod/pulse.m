#include "clock.h"
#include "edge.h"

impl Pulse
{
    in u64 period_ns;
    in boolean reset;

    mod Clock clk = {
        .reset = reset,
        .period_ns = period_ns
    };

    mod Edge edge = {
        .reset = reset,
        .rising = TRUE,
        .input = clk.output
    };

    out boolean output = edge.output;
};