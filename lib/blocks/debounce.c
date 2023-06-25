#include <time.h>
#include "debounce.h"

void block_Debounce(struct Debounce* self)
{
    bool s  = self->input;
    bool r  = self->reset;
    int  d  = self->duration;
    bool c  = self->current;
    int  t  = self->last_state_change;

    bool reset = block_reset();
    int now = clock();
    int duration_elapsed = (now - t) > d;
    bool signal_steady = s == c;

    if (reset)
    {
        struct Debounce init = {};
        *self = init;
    }
    else if (signal_steady && duration_elapsed)
    {
        self->current = s;
        self->output = s;
    }
    else if (signal_steady)
    {
        /* do nothing */
    }
    else
    {
        self->last_state_change = now;
    }
}
