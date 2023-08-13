// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// Drives a 7 segment display
// -----------------------------------------------------------------------------
#ifndef SEG7_H
#define SEG7_H

decl Seg7
{
    in boolean reset;
    
    out boolean refresh;
    out boolean top;
    out boolean topl;
    out boolean mid;
    out boolean topr;
    out boolean botl;
    out boolean bot;
    out boolean botr;
};

#endif // SEG7_H 
