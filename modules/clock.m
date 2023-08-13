#include "clock.h"

impl Clock
{
    const u64 TIME_BASE_REG = 1234;
    const u64 TICKS_PER_NS = 123;
    const u64 TICKS_PER_US = 123456;
    const u64 TICKS_PER_MS = 123456789;
    const u64 PERIOD_DIVISOR = 2;

    in boolean reset;
    in u64 period_in_ticks;
    
    mod TBR tbr = {.now = TRUE};
    
    var u64 half_period = div(period_in_ticks,PERIOD_DIVISOR);
    var u64 ticks_now = tbr.value;
    var u64 half_period_rem = rem(ticks_now,half_period);
    var u64 period_rem = rem(ticks_now,period_in_ticks);

    out boolean signal = eq(period_rem,half_period_rem);
};
