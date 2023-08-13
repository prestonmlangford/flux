#include "flux.h"
#include "gte.h"

boolean u8_gte(u8 a, u8 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}

boolean i8_gte(i8 a, i8 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}

boolean u16_gte(u16 a, u16 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}

boolean i16_gte(i16 a, i16 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}

boolean u32_gte(u32 a, u32 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}

boolean i32_gte(i32 a, i32 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}

boolean u64_gte(u64 a, u64 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}

boolean i64_gte(i64 a, i64 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}
