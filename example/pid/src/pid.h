#ifndef PID_H
#define PID_H
#include "flux.h"


struct Pid
{
    boolean reset;
    i32 r;
    i32 y;
    i32 Kp;
    i32 Ki;
    i32 Kd;
    i32 e;
    i32 i;
    i32 d;
    i32 i_prev;
    i32 e_prev;
    i32 u;
};

void module_pid(struct Pid* self);
#endif /* PID_H */
