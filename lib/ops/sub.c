#include "flux.h"
#include "sub.h"

u8 u8_sub(u8 a, u8 b)
{
    u8 result = {};
    bool okay = a.valid && b.valid && (a.value >= b.value);

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }

    return result;
}

i8 i8_sub(i8 a, i8 b)
{
    i8 result = {};
    bool okay = a.valid && b.valid;

    if (b.value > INT8_C(0))
    {
        int8_t limit = INT8_MIN + b.value;
        okay = okay && (a.value >= limit);
    }
    else if (b.value < INT8_C(0))
    {
        int8_t limit = INT8_MAX + b.value;
        okay = okay && (a.value <= limit);
    }
    else
    {
        /* Do nothing. */
    }

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }
    
    return result;
}

u16 u16_sub(u16 a, u16 b)
{
    u16 result = {};
    bool okay = a.valid && b.valid && (a.value >= b.value);

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }

    return result;
}

i16 i16_sub(i16 a, i16 b)
{
    i16 result = {};
    bool okay = a.valid && b.valid;

    if (b.value > INT16_C(0))
    {
        int16_t limit = INT16_MIN + b.value;
        okay = okay && (a.value >= limit);
    }
    else if (b.value < INT16_C(0))
    {
        int16_t limit = INT16_MAX + b.value;
        okay = okay && (a.value <= limit);
    }
    else
    {
        /* Do nothing. */
    }

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }
    
    return result;
}

u32 u32_sub(u32 a, u32 b)
{
    u32 result = {};
    bool okay = a.valid && b.valid && (a.value >= b.value);

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }

    return result;
}

i32 i32_sub(i32 a, i32 b)
{
    i32 result = {};
    bool okay = a.valid && b.valid;

    if (b.value > INT32_C(0))
    {
        int32_t limit = INT32_MIN + b.value;
        okay = okay && (a.value >= limit);
    }
    else if (b.value < INT32_C(0))
    {
        int32_t limit = INT32_MAX + b.value;
        okay = okay && (a.value <= limit);
    }
    else
    {
        /* Do nothing. */
    }

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }
    
    return result;
}

u64 u64_sub(u64 a, u64 b)
{
    u64 result = {};
    bool okay = a.valid && b.valid && (a.value >= b.value);

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }

    return result;
}

i64 i64_sub(i64 a, i64 b)
{
    i64 result = {};
    bool okay = a.valid && b.valid;

    if (b.value > INT64_C(0))
    {
        int64_t limit = INT64_MIN + b.value;
        okay = okay && (a.value >= limit);
    }
    else if (b.value < INT64_C(0))
    {
        int64_t limit = INT64_MAX + b.value;
        okay = okay && (a.value <= limit);
    }
    else
    {
        /* Do nothing. */
    }

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }
    
    return result;
}
