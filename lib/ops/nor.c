#include "flux.h"
#include "nor.h"

u8 u8_nor(size_t argc, u8 argv[])
{
    u8 result = {};
    uint8_t sum = UINT8_MAX;
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
        result.value = ~sum;
        result.valid = true;
    }
    
    return result;
}

u16 u16_nor(size_t argc, u16 argv[])
{
    u16 result = {};
    uint16_t sum = UINT16_MAX;
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
        result.value = ~sum;
        result.valid = true;
    }
    
    return result;
}

u32 u32_nor(size_t argc, u32 argv[])
{
    u32 result = {};
    uint32_t sum = UINT32_MAX;
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
        result.value = ~sum;
        result.valid = true;
    }
    
    return result;
}

u64 u64_nor(size_t argc, u64 argv[])
{
    u64 result = {};
    uint64_t sum = UINT64_MAX;
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
        result.value = ~sum;
        result.valid = true;
    }
    
    return result;
}

boolean boolean_nor(size_t argc, boolean argv[])
{
    boolean result = {};
    bool sum = true;
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
        result.value = !sum;
        result.valid = true;
    }

    return result;
}
