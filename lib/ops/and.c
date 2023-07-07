#include "and.h"

boolean boolean_and(size_t argc, boolean argv[])
{
    bool result = true;
    bool valid = true;
    size_t i;

    for (i = 0U; i < argc; i++)
    {
        result = result && argv[i].value;
        valid = valid && argv[i].valid;
    }

    return (boolean){result,valid};
}

u32 u32_and(size_t argc, u32 argv[])
{
    uint32_t value = UINT32_MAX;
    bool valid = true;
    u32 result = {};
    size_t i;

    for (i = 0U; i < argc; i++)
    {
        value = value & argv[i].value;
        valid = valid && argv[i].valid;
    }
    
    result.value = value;
    result.valid = valid;
    
    return result;
}
