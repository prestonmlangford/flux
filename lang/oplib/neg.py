
decl_u = ""
impl_u = ""

decl_i = """
i$ i$_neg(i$ x);
"""

impl_i = """
i$ i$_neg(i$ x)
{
    i$ result = {};

    if (x.valid && (x.value != INT$_MIN))
    {
        result.value = -x.value;
        result.valid = true;
    }

    return result;
}
"""

decl_f = ""
impl_f = ""

decl_b = ""
impl_b = ""
