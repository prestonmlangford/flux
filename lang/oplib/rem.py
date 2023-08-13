
decl = """
u$ u$_rem(u$ a, u$ b);
i$ i$_rem(i$ a, i$ b);
"""

decl_u = """
u$ u$_rem(u$ a, u$ b);
"""

impl_u = """
u$ u$_rem(u$ a, u$ b)
{
    u$ result = {};
    bool divide_by_zero = b.value == INT$_C(0);

    if (a.valid && b.valid && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }
    
    return result;
}
"""

decl_i = """
i$ i$_rem(i$ a, i$ b);
"""

impl_i = """
i$ i$_rem(i$ a, i$ b)
{
    i$ result = {};
    bool divide_by_zero = b.value == INT$_C(0);
    bool overflow = (a.value == INT$_MIN) && (b.value == INT$_C(-1));

    if (a.valid && b.valid && (!overflow) && (!divide_by_zero))
    {
        result.value = a.value % b.value;
        result.valid = true;
    }

    return result;
}
"""

decl_f = ""
impl_f = ""

decl_b = ""
impl_b = ""