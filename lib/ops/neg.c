#include "flux.h"
#include "neg.h"

i8 i8_neg(i8 x)
{
    i8 result = {};

    if (x.valid && (x.value != INT8_MIN))
    {
        result.value = -x.value;
        result.valid = true;
    }

    return result;
}

i16 i16_neg(i16 x)
{
    i16 result = {};

    if (x.valid && (x.value != INT16_MIN))
    {
        result.value = -x.value;
        result.valid = true;
    }

    return result;
}

i32 i32_neg(i32 x)
{
    i32 result = {};

    if (x.valid && (x.value != INT32_MIN))
    {
        result.value = -x.value;
        result.valid = true;
    }

    return result;
}

i64 i64_neg(i64 x)
{
    i64 result = {};

    if (x.valid && (x.value != INT64_MIN))
    {
        result.value = -x.value;
        result.valid = true;
    }

    return result;
}
