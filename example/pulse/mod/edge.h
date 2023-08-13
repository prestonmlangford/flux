// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// Detects edges on a boolean signal
// -----------------------------------------------------------------------------
#ifndef EDGE_H
#define EDGE_H

decl Edge
{
    in boolean reset;
    in boolean rising;
    in boolean input;
    out boolean output;
};

#endif // EDGE_H 
