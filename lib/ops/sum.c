#include "flux.h"
#include "sum.h"

u8 u8_sum(size_t argc, u8 argv[])
{
    u8 result = {};
    uint8_t sum = UINT8_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint8_t term = argv[i].value;
            uint8_t limit = UINT8_MAX - term;

            okay = okay && argv[i].valid;
            okay = okay && (sum <= limit);

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}

i8 i8_sum(size_t argc, i8 argv[])
{
    i8 result = {};
    int8_t sum = INT8_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int8_t term = argv[i].value;
            okay = okay && argv[i].valid;
            
            if (term > INT8_C(0))
            {
                int8_t limit = INT8_MAX - term;
                okay = okay && (sum <= limit);
            }
            else if (term < INT8_C(0))
            {
                int8_t limit = INT8_MIN - term;
                okay = okay && (sum >= limit);
            }
            else
            {
                /* Do nothing. */
            }

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}

u16 u16_sum(size_t argc, u16 argv[])
{
    u16 result = {};
    uint16_t sum = UINT16_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint16_t term = argv[i].value;
            uint16_t limit = UINT16_MAX - term;

            okay = okay && argv[i].valid;
            okay = okay && (sum <= limit);

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}

i16 i16_sum(size_t argc, i16 argv[])
{
    i16 result = {};
    int16_t sum = INT16_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int16_t term = argv[i].value;
            okay = okay && argv[i].valid;
            
            if (term > INT16_C(0))
            {
                int16_t limit = INT16_MAX - term;
                okay = okay && (sum <= limit);
            }
            else if (term < INT16_C(0))
            {
                int16_t limit = INT16_MIN - term;
                okay = okay && (sum >= limit);
            }
            else
            {
                /* Do nothing. */
            }

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}

u32 u32_sum(size_t argc, u32 argv[])
{
    u32 result = {};
    uint32_t sum = UINT32_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint32_t term = argv[i].value;
            uint32_t limit = UINT32_MAX - term;

            okay = okay && argv[i].valid;
            okay = okay && (sum <= limit);

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}

i32 i32_sum(size_t argc, i32 argv[])
{
    i32 result = {};
    int32_t sum = INT32_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int32_t term = argv[i].value;
            okay = okay && argv[i].valid;
            
            if (term > INT32_C(0))
            {
                int32_t limit = INT32_MAX - term;
                okay = okay && (sum <= limit);
            }
            else if (term < INT32_C(0))
            {
                int32_t limit = INT32_MIN - term;
                okay = okay && (sum >= limit);
            }
            else
            {
                /* Do nothing. */
            }

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}

u64 u64_sum(size_t argc, u64 argv[])
{
    u64 result = {};
    uint64_t sum = UINT64_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint64_t term = argv[i].value;
            uint64_t limit = UINT64_MAX - term;

            okay = okay && argv[i].valid;
            okay = okay && (sum <= limit);

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}

i64 i64_sum(size_t argc, i64 argv[])
{
    i64 result = {};
    int64_t sum = INT64_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int64_t term = argv[i].value;
            okay = okay && argv[i].valid;
            
            if (term > INT64_C(0))
            {
                int64_t limit = INT64_MAX - term;
                okay = okay && (sum <= limit);
            }
            else if (term < INT64_C(0))
            {
                int64_t limit = INT64_MIN - term;
                okay = okay && (sum >= limit);
            }
            else
            {
                /* Do nothing. */
            }

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}
