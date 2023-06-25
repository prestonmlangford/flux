#include <stdio.h>
#include "types.h"
#include "landing.h"


int main()
{
    struct Landing_State landing = {};

    while (1)
    {
        struct Landing_Input input = 
        {
            .master_reset = false,
            .wow = false,
        };
        process_landing(&input, &landing);
    }

    return 0;
}