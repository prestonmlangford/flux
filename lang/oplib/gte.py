
decl_u = """
boolean u$_gte(u$ a, u$ b);
"""

impl_u = """
boolean u$_gte(u$ a, u$ b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}
"""

decl_i = """
boolean i$_gte(i$ a, i$ b);
"""

impl_i = """
boolean i$_gte(i$ a, i$ b)
{
    boolean result = {};

    if (a.valid && b.valid)
    {
        result.value = a.value >= b.value;
        result.valid = true;
    }

    return result;
}
"""

decl_f = ""
impl_f = ""

decl_b = ""
impl_b = ""
