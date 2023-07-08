decl Sbm
{
    const u32 ADDR_THERMAL;
    const i32 XA01;

    in i32 id;
    in u32 address;
    
    in boolean read;
    out u32 rval;

    in boolean write;
    in u32 wval;
};

decl Ticker
{
    in i64 period;
    in bool reset;
    out bool tick;
};

decl Clock
{
    const u64 TICKS_PER_NS;
    const u64 TICKS_PER_US;
    const u64 TICKS_PER_MS;

    in boolean reset;
    in u64 period_in_ticks;
    out boolean signal;
};

decl Hysteresis
{
    in f32 input;
    in f32 tolerance;
    out f32 output;
};

impl Clock
{
    const u64 TIME_BASE_REG = u64(1234);
    const u64 TICKS_PER_NS = u64(123);
    const u64 TICKS_PER_US = u64(123456);
    const u64 TICKS_PER_MS = u64(123456789);

    in boolean reset;
    in u64 period_in_ticks;

    var u64 half_period = div(period_in_ticks,u64(2));
    var u64 ticks_now = TIME_BASE_REG;
    var u64 half_period_rem = rem(ticks_now,half_period);
    var u64 period_rem = rem(ticks_now,period_in_ticks);

    out boolean signal = eq(period_rem,half_period_rem);
};

decl Edge
{
    in boolean reset;
    in boolean rising;
    in boolean input;
    out boolean output;
};

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

decl Pulse
{
    in u64 period_ms;
    in bool reset;

    out bool signal;
};

impl Pulse
{
    in u64 period_ms;
    in bool reset;

    mod Clock clk = {
        .reset = reset,
        .period_in_ticks = mul(Clock::TICKS_PER_MS,period_ms)
    };

    mod Edge edge = {
        .reset = reset,
        .rising = boolean(1),
        .input = clk.signal
    };

    out bool signal = edge.output;
};

decl Sbm_Thermal_Monitor
{
    const u32 THERMAL_REG_MASK;
    const f32 TEMPERATURE_SCALE;
    const f32 STATUS_PERIOD;
    
    in bool reset;
    out f32 temperature;
};

impl Sbm_Thermal_Monitor
{
    const u32 THERMAL_REG_MASK = u32(12345);
    const f32 TEMPERATURE_SCALE = f32(123);
    const f32 STATUS_PERIOD = u64(10);
    
    in bool reset;

    mod Pulse poll_100hz = {
        .reset = reset,
        .period_ms = STATUS_PERIOD
    };

    mod Sbm thermal = {
        .address = Sbm::ADDR_THERMAL,
        .id = Sbm::XA01,
        .read = poll_100hz.signal
    };

    var u32 temperature_bits = and(thermal.rval,Sbm_Thermal_Monitor::THERMAL_REG_MASK);
    var f32 temperature_prescaled = cast(temperature_bits);

    mod Hysteresis hyst = {
        .input = mul(temperature_prescaled,Sbm_Thermal_Monitor::TEMPERATURE_SCALE),
        .tolerance = f32(5)
    };

    out f32 temperature = hyst.output;
};
