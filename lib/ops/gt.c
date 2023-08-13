#include "flux.h"
#include "gt.h"

boolean u8_gt(u8 a, u8 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value > b.value;
        result.valid = true;
    }

    return result;
}

boolean i8_gt(i8 a, i8 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value > b.value;
        result.valid = true;
    }

    return result;
}

boolean u16_gt(u16 a, u16 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value > b.value;
        result.valid = true;
    }

    return result;
}

boolean i16_gt(i16 a, i16 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value > b.value;
        result.valid = true;
    }

    return result;
}

boolean u32_gt(u32 a, u32 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value > b.value;
        result.valid = true;
    }

    return result;
}

boolean i32_gt(i32 a, i32 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value > b.value;
        result.valid = true;
    }

    return result;
}

boolean u64_gt(u64 a, u64 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value > b.value;
        result.valid = true;
    }

    return result;
}

boolean i64_gt(i64 a, i64 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value > b.value;
        result.valid = true;
    }

    return result;
}
