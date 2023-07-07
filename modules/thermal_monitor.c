#include <stdint.h>

typedef enum {false,true} bool;

#define in
#define out
#define var
#define mod
#define decl struct
#define impl struct

#define DECL_SIGNAL(name,ctype) typedef struct name {ctype value;bool valid;} name

DECL_SIGNAL(i64, int64_t);
DECL_SIGNAL(u64,uint64_t);
DECL_SIGNAL(i32, int32_t);
DECL_SIGNAL(u32,uint32_t);
DECL_SIGNAL(i16, int16_t);
DECL_SIGNAL(u16,uint16_t);
DECL_SIGNAL( i8,  int8_t);
DECL_SIGNAL( u8, uint8_t);

DECL_SIGNAL(f32, float);
DECL_SIGNAL(f64, double);

DECL_SIGNAL(boolean, bool);

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

impl Clock
{
    const u64 TICKS_PER_NS = u64(123);
    const u64 TICKS_PER_US = u64(123456);
    const u64 TICKS_PER_MS = u64(123456789);

    in boolean reset;
    in u64 period_in_ticks;

    var u64 half_period = div(period_in_ticks,i64(2));
    var u64 ticks_now = tbr();
    var u64 half_period_rem = rem(ticks_now,half_period);
    var u64 period_rem = rem(ticks_now,period_in_ticks);

    out boolean signal = eq(period_rem,half_period_rem);
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
        .rising = boolean(true),
        .input = clk.signal
    };

    out bool signal = edge.output;
};

impl Sbm_Thermal_Monitor
{
    const u32 THERMAL_REG_MASK = u32(0x000001FF);
    const f32 TEMPERATURE_SCALE = f32(0.123);
    
    in bool reset;

    mod Pulse poll_100hz = {
        .reset = reset,
        .period_ms = i64(10)
    };

    mod Sbm thermal = {
        .address = Sbm::ADDR_THERMAL,
        .id = Sbm::XA01
        .read = poll_100hz.signal,
    };

    var u32 temperature_bits = and(thermal.rval,THERMAL_REG_MASK);
    var f32 temperature_prescaled = u32_f32(temperature_bits);
    var f32 temperature_raw = mul(temperature_prescaled,TEMPERATURE_SCALE);

    mod Hysteresis hyst = {
        .input = temperature_raw,
        .tolerance = f32(5.0)
    };

    out temperature = hyst.output;
};