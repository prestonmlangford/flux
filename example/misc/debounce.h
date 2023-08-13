// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// This module debounces a boolean signal
// -----------------------------------------------------------------------------
#ifndef DEBOUNCE_H
#define DEBOUNCE_H

decl u32 dev_read(i23 id, u32 reg); 

decl module Debounce
{
    in bool reset;
    in bool input;
    in i64 duration;

    out bool output;
};

#endif // DEBOUNCE_H 
