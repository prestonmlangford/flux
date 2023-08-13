#include "flux.h"
#include "rem.h"

u8 u8_rem(u8 a, u8 b)
{
    u8 result = {};
    bool divide_by_zero = b.value == INT8_C(0);

    if (a.valid && b.valid && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }
    
    return result;
}

i8 i8_rem(i8 a, i8 b)
{
    i8 result = {};
    bool divide_by_zero = b.value == INT8_C(0);
    bool overflow = (a.value == INT8_MIN) && (b.value == INT8_C(-1));

    if (a.valid && b.valid && (!overflow) && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }

    return result;
}

u16 u16_rem(u16 a, u16 b)
{
    u16 result = {};
    bool divide_by_zero = b.value == INT16_C(0);

    if (a.valid && b.valid && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }
    
    return result;
}

i16 i16_rem(i16 a, i16 b)
{
    i16 result = {};
    bool divide_by_zero = b.value == INT16_C(0);
    bool overflow = (a.value == INT16_MIN) && (b.value == INT16_C(-1));

    if (a.valid && b.valid && (!overflow) && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }

    return result;
}

u32 u32_rem(u32 a, u32 b)
{
    u32 result = {};
    bool divide_by_zero = b.value == INT32_C(0);

    if (a.valid && b.valid && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }
    
    return result;
}

i32 i32_rem(i32 a, i32 b)
{
    i32 result = {};
    bool divide_by_zero = b.value == INT32_C(0);
    bool overflow = (a.value == INT32_MIN) && (b.value == INT32_C(-1));

    if (a.valid && b.valid && (!overflow) && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }

    return result;
}

u64 u64_rem(u64 a, u64 b)
{
    u64 result = {};
    bool divide_by_zero = b.value == INT64_C(0);

    if (a.valid && b.valid && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }
    
    return result;
}

i64 i64_rem(i64 a, i64 b)
{
    i64 result = {};
    bool divide_by_zero = b.value == INT64_C(0);
    bool overflow = (a.value == INT64_MIN) && (b.value == INT64_C(-1));

    if (a.valid && b.valid && (!overflow) && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }

    return result;
}
