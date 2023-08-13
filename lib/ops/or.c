#include "flux.h"
#include "or.h"

u8 u8_or(size_t argc, u8 argv[])
{
    u8 result = {};
    uint8_t sum = UINT8_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                sum = sum | argv[i].value;
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

u16 u16_or(size_t argc, u16 argv[])
{
    u16 result = {};
    uint16_t sum = UINT16_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                sum = sum | argv[i].value;
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

u32 u32_or(size_t argc, u32 argv[])
{
    u32 result = {};
    uint32_t sum = UINT32_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                sum = sum | argv[i].value;
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

u64 u64_or(size_t argc, u64 argv[])
{
    u64 result = {};
    uint64_t sum = UINT64_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                sum = sum | argv[i].value;
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

boolean boolean_or(size_t argc, boolean argv[])
{
    boolean result = {};
    bool sum = false;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                sum = sum || argv[i].value;
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
