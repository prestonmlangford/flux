
decl_u = """
u$ u$_mux(boolean s, u$ a, u$ b);
"""

impl_u = """
u$ u$_mux(boolean s, u$ a, u$ b)
{
    u$ result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}
"""

decl_i = """
i$ i$_mux(boolean s, i$ a, i$ b);
"""

impl_i = """
i$ i$_mux(boolean s, i$ a, i$ b)
{
    i$ result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}
"""
decl_f = ""
impl_f = ""

decl_b = """
boolean boolean_and(size_t argc, boolean argv[]);
"""

impl_b = """
boolean boolean_mux(boolean s, boolean a, boolean b)
{
    boolean result = {};

    if (s.valid)
    {
        if (s.value)
        {
            result = a;
        }
        else
        {
            result = b;
        }
    }

    return result;
}
"""
