#include "flux.h"
#include "xor.h"

u8 u8_xor(size_t argc, u8 argv[])
{
    u8 result = {};
    uint8_t product = UINT8_MAX;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                product = product ^ argv[i].value;
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

u16 u16_xor(size_t argc, u16 argv[])
{
    u16 result = {};
    uint16_t product = UINT16_MAX;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                product = product ^ argv[i].value;
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

u32 u32_xor(size_t argc, u32 argv[])
{
    u32 result = {};
    uint32_t product = UINT32_MAX;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                product = product ^ argv[i].value;
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

u64 u64_xor(size_t argc, u64 argv[])
{
    u64 result = {};
    uint64_t product = UINT64_MAX;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                product = product ^ argv[i].value;
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

boolean boolean_xor(size_t argc, boolean argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                product = product != argv[i].value;
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
