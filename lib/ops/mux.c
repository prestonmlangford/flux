#include "flux.h"
#include "mux.h"

u8 u8_mux(boolean s, u8 a, u8 b)
{
    u8 result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}

i8 i8_mux(boolean s, i8 a, i8 b)
{
    i8 result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}

u16 u16_mux(boolean s, u16 a, u16 b)
{
    u16 result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}

i16 i16_mux(boolean s, i16 a, i16 b)
{
    i16 result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}

u32 u32_mux(boolean s, u32 a, u32 b)
{
    u32 result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}

i32 i32_mux(boolean s, i32 a, i32 b)
{
    i32 result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}

u64 u64_mux(boolean s, u64 a, u64 b)
{
    u64 result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}

i64 i64_mux(boolean s, i64 a, i64 b)
{
    i64 result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}

boolean boolean_mux(boolean s, boolean a, boolean b)
{
    boolean result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}
