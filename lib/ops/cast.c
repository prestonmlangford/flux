#include "flux.h"
#include "cast.h"

i8 i8_not(i8 x)
{
    i8 result = {};

    if (x.valid)
    {
        result.value = ~x.value;
        result.valid = true;
    }

    return result;
}

i16 i16_not(i16 x)
{
    i16 result = {};

    if (x.valid)
    {
        result.value = ~x.value;
        result.valid = true;
    }

    return result;
}

i32 i32_not(i32 x)
{
    i32 result = {};

    if (x.valid)
    {
        result.value = ~x.value;
        result.valid = true;
    }

    return result;
}

i64 i64_not(i64 x)
{
    i64 result = {};

    if (x.valid)
    {
        result.value = ~x.value;
        result.valid = true;
    }

    return result;
}

boolean boolean_not(boolean x)
{
    boolean result = {};

    if (x.valid)
    {
        result.value = !x.value;
        result.valid = true;
    }

    return result;
}
