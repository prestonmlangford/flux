#include "flux.h"
#include "lt.h"

boolean u8_lt(u8 a, u8 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value < b.value;
        result.valid = true;
    }

    return result;
}

boolean i8_lt(i8 a, i8 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value < b.value;
        result.valid = true;
    }

    return result;
}

boolean u16_lt(u16 a, u16 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value < b.value;
        result.valid = true;
    }

    return result;
}

boolean i16_lt(i16 a, i16 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value < b.value;
        result.valid = true;
    }

    return result;
}

boolean u32_lt(u32 a, u32 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value < b.value;
        result.valid = true;
    }

    return result;
}

boolean i32_lt(i32 a, i32 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value < b.value;
        result.valid = true;
    }

    return result;
}

boolean u64_lt(u64 a, u64 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value < b.value;
        result.valid = true;
    }

    return result;
}

boolean i64_lt(i64 a, i64 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value < b.value;
        result.valid = true;
    }

    return result;
}
