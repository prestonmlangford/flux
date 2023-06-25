#ifndef DEBOUNCE_H
#define DEBOUNCE_H

#include "types.h"

struct Debounce
{
    /* inputs */
    bool reset;
    bool input;
    int duration;

    /* states */
    bool current;
    int last_state_change;
    
    /* outputs */
    bool output;
};

void block_Debounce(struct Debounce* self);

#endif /* DEBOUNCE_H */
