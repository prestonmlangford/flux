#include "and.h"

boolean boolean_and(size_t argc, boolean argv[])
{
    bool value = true;
    bool valid = true;
    size_t i;

    for (i = 0U; i < argc; i++)
    {
        value = value && argv[i].value;
        valid = valid && argv[i].valid;
    }

    return (boolean){value,valid};
}

u32 u32_and(size_t argc, u32 argv[])
{
    uint32_t value = UINT32_MAX;
    bool valid = true;
    size_t i;

    for (i = 0U; i < argc; i++)
    {
        value = value & argv[i].value;
        valid = valid && argv[i].valid;
    }

    return (u32){value,valid};
}
