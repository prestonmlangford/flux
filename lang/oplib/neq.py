
decl_u = """
boolean u$_neq(size_t argc, u$ argv[]);
"""

impl_u = """
boolean u$_neq(size_t argc, u$ argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
            }
        }
    }

    if (okay)
    {
        result.value = !product;
        result.valid = true;
    }

    return result;
}
"""

decl_i= """
boolean i$_neq(size_t argc, i$ argv[]);
"""

impl_i = """
boolean i$_neq(size_t argc, i$ argv[])
{
    boolean result = {};
    bool product = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 1U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                bool equal = argv[i - 1U].value == argv[i].value;
                product = product && equal;
            }
        }
    }

    if (okay)
    {
        result.value = !product;
        result.valid = true;
    }

    return result;
}
"""

decl_f = ""
impl_f = ""

decl_b = ""
impl_b = ""
