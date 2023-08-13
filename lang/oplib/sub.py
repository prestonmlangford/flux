
decl_u = """
u$ u$_sub(u$ a, u$ b);
"""

impl_u = """
u$ u$_sub(u$ a, u$ b)
{
    u$ result = {};
    bool okay = a.valid && b.valid && (a.value >= b.value);

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }

    return result;
}
"""

decl_i = """
i$ i$_sub(i$ a, i$ b);
"""

impl_i = """
i$ i$_sub(i$ a, i$ b)
{
    i$ result = {};
    bool okay = a.valid && b.valid;

    if (b.value > INT$_C(0))
    {
        int$_t limit = INT$_MIN + b.value;
        okay = okay && (a.value >= limit);
    }
    else if (b.value < INT$_C(0))
    {
        int$_t limit = INT$_MAX + b.value;
        okay = okay && (a.value <= limit);
    }
    else
    {
        /* Do nothing. */
    }

    if (okay)
    {
        result.value = a.value - b.value;
        result.valid = true;
    }
    
    return result;
}
"""

decl_f = ""
impl_f = ""

decl_b = ""
impl_b = ""
