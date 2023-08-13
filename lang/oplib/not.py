
decl_u = """
i$ i$_not(i$ x);
"""

impl_u = """
i$ i$_not(i$ x)
{
    i$ result = {};

    if (x.valid)
    {
        result.value = ~x.value;
        result.valid = true;
    }

    return result;
}
"""

decl_i = ""
impl_i = ""

decl_f = ""
impl_f = ""

decl_b = """
boolean boolean_not(boolean x);
"""

impl_b = """
boolean boolean_not(boolean x)
{
    boolean result = {};

    if (x.valid)
    {
        result.value = !x.value;
        result.valid = true;
    }

    return result;
}
"""
