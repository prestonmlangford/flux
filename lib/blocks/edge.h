#ifndef SINGLE_SHOT_H
#define SINGLE_SHOT_H

#include "types.h"

struct Edge
{
    bool reset;
    bool signal;
    bool rising;
    bool last;
    bool output;
};

void block_Edge(struct Edge* self);

#endif /* SINGLE_SHOT_H */
