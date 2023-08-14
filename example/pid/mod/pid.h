// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// Drives a 7 segment display
// -----------------------------------------------------------------------------
#ifndef PID_H
#define PID_H

decl Pid
{
    in boolean reset;
    in i32 r;
    in i32 y;
    in i32 Kp;
    in i32 Ki;
    in i32 Kd;
    
    out i32 u;
};

#endif // PID_H
