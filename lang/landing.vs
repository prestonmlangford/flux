

block Debounce
{
    in bool input;
    in u64 duration;
    out bool output;
};

block Hw_Register
{
    in bool now;
    out u32 reg;
};

block Subaddress
{
    in bool now;
    out u16 words[32];
};

block Edge
{
    in bool input;
    in bool rising;
    out bool output;
};

module Landing
{
    in i32 fuel;
    in bool wow;
    in bool flight;

    module Coordinates coor = 
    {
        .now = bool(1)
    };

    block Debounce db = 
    {
        .input = wow,
        .duration = i64(123)
    };

    block Edge edge =
    {
        .input = db.result,
        .rising = bool(0)
    };

    var bool transit = not(flight);
    var f64 larpitude[2] = sum(coor.latitude, 
                               coor.longitude);
    out bool stop = db.result;
    out bool start = and(db.output,edge.output,transit);
};
