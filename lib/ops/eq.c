#include "flux.h"
#include "eq.h"

boolean u8_eq(size_t argc, u8 argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
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

boolean i8_eq(size_t argc, i8 argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
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

boolean u16_eq(size_t argc, u16 argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
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

boolean i16_eq(size_t argc, i16 argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
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

boolean u32_eq(size_t argc, u32 argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
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

boolean i32_eq(size_t argc, i32 argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
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

boolean u64_eq(size_t argc, u64 argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
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

boolean i64_eq(size_t argc, i64 argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
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
