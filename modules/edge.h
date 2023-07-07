// -----------------------------------------------------------------------------
// Copyright 25 June 2023
// Author: Preston Langford
// This module detects edges on a boolean signal
// -----------------------------------------------------------------------------
#ifndef EDGE_H
#define EDGE_H

decl module Edge
{
    in bool reset;
    in bool input;
    in bool rising;
    out bool output;
};

#endif // EDGE_H 
