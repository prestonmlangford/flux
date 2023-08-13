#include "tick.h"
#include "clock.h"

impl Clock
{
    in boolean reset;
    in u64 period_ns;
    const u64 PERIOD_DIVISOR = 2;

    mod Tick t = {.reset = reset};

    var u64 half_period = div(period_ns, PERIOD_DIVISOR);
    var u64 ticks_now = t.ticks;
    var u64 half_period_rem = rem(ticks_now,half_period);
    var u64 period_rem = rem(ticks_now,period_ns);

    out boolean output = eq(period_rem,half_period_rem);
};
