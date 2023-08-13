#include "flux.h"
#include "lte.h"

boolean u8_lte(u8 a, u8 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value <= b.value;
        result.valid = true;
    }

    return result;
}

boolean i8_lte(i8 a, i8 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value <= b.value;
        result.valid = true;
    }

    return result;
}

boolean u16_lte(u16 a, u16 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value <= b.value;
        result.valid = true;
    }

    return result;
}

boolean i16_lte(i16 a, i16 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value <= b.value;
        result.valid = true;
    }

    return result;
}

boolean u32_lte(u32 a, u32 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value <= b.value;
        result.valid = true;
    }

    return result;
}

boolean i32_lte(i32 a, i32 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value <= b.value;
        result.valid = true;
    }

    return result;
}

boolean u64_lte(u64 a, u64 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value <= b.value;
        result.valid = true;
    }

    return result;
}

boolean i64_lte(i64 a, i64 b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value <= b.value;
        result.valid = true;
    }

    return result;
}
