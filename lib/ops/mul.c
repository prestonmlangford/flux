#include "flux.h"
#include "mul.h"

u8 u8_mul(size_t argc, u8 argv[])
{
    u8 result = {};
    uint8_t product = UINT8_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint8_t a = product;
            uint8_t b = argv[i].value;

            okay = okay && argv[i].valid;

            if (b > UINT8_C(0))
            {
                int8_t limit = UINT8_MAX / b;
                okay = okay && (a <= limit);
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}

i8 i8_mul(size_t argc, i8 argv[])
{
    i8 result = {};
    int8_t product = INT8_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int8_t a = product;
            int8_t b = argv[i].value;
            bool a_pos = a > INT8_C(0);
            bool b_pos = b > INT8_C(0);

            okay = okay && argv[i].valid;

            if (a_pos)
            {
                if (b_pos)
                {
                    int8_t limit = INT8_MAX / b;
                    okay = okay && (a <= limit);
                }
                else
                {
                    int8_t limit = INT8_MIN / a;
                    okay = okay && (b >= limit);
                }
            }
            else
            {
                if (b_pos)
                {
                    int8_t limit = INT8_MIN / b;
                    okay = okay && (a >= limit);
                }
                else if (a != INT8_C(0))
                {
                    int8_t limit = INT8_MAX / a;
                    okay = okay && (b >= limit);
                }
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}

u16 u16_mul(size_t argc, u16 argv[])
{
    u16 result = {};
    uint16_t product = UINT16_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint16_t a = product;
            uint16_t b = argv[i].value;

            okay = okay && argv[i].valid;

            if (b > UINT16_C(0))
            {
                int16_t limit = UINT16_MAX / b;
                okay = okay && (a <= limit);
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}

i16 i16_mul(size_t argc, i16 argv[])
{
    i16 result = {};
    int16_t product = INT16_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int16_t a = product;
            int16_t b = argv[i].value;
            bool a_pos = a > INT16_C(0);
            bool b_pos = b > INT16_C(0);

            okay = okay && argv[i].valid;

            if (a_pos)
            {
                if (b_pos)
                {
                    int16_t limit = INT16_MAX / b;
                    okay = okay && (a <= limit);
                }
                else
                {
                    int16_t limit = INT16_MIN / a;
                    okay = okay && (b >= limit);
                }
            }
            else
            {
                if (b_pos)
                {
                    int16_t limit = INT16_MIN / b;
                    okay = okay && (a >= limit);
                }
                else if (a != INT16_C(0))
                {
                    int16_t limit = INT16_MAX / a;
                    okay = okay && (b >= limit);
                }
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}

u32 u32_mul(size_t argc, u32 argv[])
{
    u32 result = {};
    uint32_t product = UINT32_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint32_t a = product;
            uint32_t b = argv[i].value;

            okay = okay && argv[i].valid;

            if (b > UINT32_C(0))
            {
                int32_t limit = UINT32_MAX / b;
                okay = okay && (a <= limit);
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}

i32 i32_mul(size_t argc, i32 argv[])
{
    i32 result = {};
    int32_t product = INT32_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int32_t a = product;
            int32_t b = argv[i].value;
            bool a_pos = a > INT32_C(0);
            bool b_pos = b > INT32_C(0);

            okay = okay && argv[i].valid;

            if (a_pos)
            {
                if (b_pos)
                {
                    int32_t limit = INT32_MAX / b;
                    okay = okay && (a <= limit);
                }
                else
                {
                    int32_t limit = INT32_MIN / a;
                    okay = okay && (b >= limit);
                }
            }
            else
            {
                if (b_pos)
                {
                    int32_t limit = INT32_MIN / b;
                    okay = okay && (a >= limit);
                }
                else if (a != INT32_C(0))
                {
                    int32_t limit = INT32_MAX / a;
                    okay = okay && (b >= limit);
                }
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}

u64 u64_mul(size_t argc, u64 argv[])
{
    u64 result = {};
    uint64_t product = UINT64_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint64_t a = product;
            uint64_t b = argv[i].value;

            okay = okay && argv[i].valid;

            if (b > UINT64_C(0))
            {
                int64_t limit = UINT64_MAX / b;
                okay = okay && (a <= limit);
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}

i64 i64_mul(size_t argc, i64 argv[])
{
    i64 result = {};
    int64_t product = INT64_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int64_t a = product;
            int64_t b = argv[i].value;
            bool a_pos = a > INT64_C(0);
            bool b_pos = b > INT64_C(0);

            okay = okay && argv[i].valid;

            if (a_pos)
            {
                if (b_pos)
                {
                    int64_t limit = INT64_MAX / b;
                    okay = okay && (a <= limit);
                }
                else
                {
                    int64_t limit = INT64_MIN / a;
                    okay = okay && (b >= limit);
                }
            }
            else
            {
                if (b_pos)
                {
                    int64_t limit = INT64_MIN / b;
                    okay = okay && (a >= limit);
                }
                else if (a != INT64_C(0))
                {
                    int64_t limit = INT64_MAX / a;
                    okay = okay && (b >= limit);
                }
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}
