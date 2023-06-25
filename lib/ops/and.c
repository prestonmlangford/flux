#include <time.h>
#include "and.h"

bool op_and(bool argv[], size_t argc)
{
    bool result = true;
    size_t i = 0U;

    while (i < argc)
    {
        result = result && argv[i];
        i += 1U;
    }

    return result;
}
