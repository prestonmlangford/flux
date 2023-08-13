#include <stdio.h>
#include "flux.h"
#include "pulse.h"

int main()
{
    struct Pulse pulse = 
    {
        .reset = TRUE,
        .period_ns = U64(1000000000),
    };

    while (1)
    {
        module_pulse(&pulse);
        pulse.reset = FALSE;

        if (pulse.output.value)
        {
            printf("pulse\n");
        }
    }

    return 0;
}