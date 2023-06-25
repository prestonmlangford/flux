#include "edge.h"

void block_Edge(struct Edge* self)
{
    bool signal = self->signal;
    bool reset  = self->reset;
    bool rising = self->rising;
    bool last   = self->last;

    if (reset)
    {
        struct Edge init = {};
        *self = init;
    }
    else if (rising)
    {
        self->last = signal;
        self->output = !last && signal;
    }
    else
    {
        self->last = signal;
        self->output = last && !signal;
    }
}
