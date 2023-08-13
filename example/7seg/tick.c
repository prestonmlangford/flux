#include "time.h"
#include "tick.h"

#define NSEC_PER_SEC 1000000000ULL

void module_tick(struct Tick* self)
{
    if (self != NULL)
    {
        bool reset = self->reset.value && self->reset.valid;
        struct timespec ts = {};
        int result = clock_gettime(CLOCK_MONOTONIC, &ts);
        uint64_t s = (uint64_t) ts.tv_sec;
        uint64_t ns = (uint64_t) ts.tv_nsec;
        u64 t = VALID((s * NSEC_PER_SEC) + ns);
        bool valid = self->reset.valid && self->start.valid && (result == 0);

        if (reset)
        {
            self->output = U64(0);
            self->start = t;
        }
        else if (valid)
        {
            self->output = u64_sub(t, self->start);
        }
        else
        {
            self->output = U64_INVALID;
            self->start = U64_INVALID;
        }
    }
};
