#include "tick.h"

impl Seg7
{
    in boolean reset;
    const u64 NS_PER_SEC = 1000000000;
    const u64 BASE_10 = 10;
    
    const u64 DIG_0 = 0;
    const u64 DIG_1 = 1;
    const u64 DIG_2 = 2;
    const u64 DIG_3 = 3;
    const u64 DIG_4 = 4;
    const u64 DIG_5 = 5;
    const u64 DIG_6 = 6;
    const u64 DIG_7 = 7;
    const u64 DIG_8 = 8;
    const u64 DIG_9 = 9;

    mod Tick t = {.reset = reset};
    var u64 seconds = div(t.output, NS_PER_SEC);
    var u64 digit = rem(seconds,BASE_10);
    out boolean refresh = not(eq(last,digit));
    var u64 last = digit;
    var boolean is_0 = eq(digit,DIG_0);
    var boolean is_1 = eq(digit,DIG_1);
    var boolean is_2 = eq(digit,DIG_2);
    var boolean is_3 = eq(digit,DIG_3);
    var boolean is_4 = eq(digit,DIG_4);
    var boolean is_5 = eq(digit,DIG_5);
    var boolean is_6 = eq(digit,DIG_6);
    var boolean is_7 = eq(digit,DIG_7);
    var boolean is_8 = eq(digit,DIG_8);
    var boolean is_9 = eq(digit,DIG_9);

    /*
     _         _    _         _    _    _    _    _ 
    | |    |   _|   _|  |_|  |_   |_     |  |_|  |_|
    |_|.   |. |_.   _|.   |.  _|. |_|.   |. |_|.  _|.

    */

    out boolean top = or(is_0,is_2,is_3,is_5,is_6,is_7,is_8,is_9);
    out boolean topl = or(is_0,is_4,is_5,is_6,is_8,is_9);
    out boolean mid = or(is_2,is_3,is_4,is_5,is_6,is_8,is_9);
    out boolean topr = or(is_0,is_1,is_2,is_3,is_4,is_7,is_8,is_9);
    out boolean botl = or(is_0,is_2,is_6,is_8);
    out boolean bot = or(is_0,is_2,is_3,is_5,is_6,is_8,is_9);
    out boolean botr = or(is_0,is_1,is_3,is_4,is_5,is_6,is_7,is_8,is_9);
};