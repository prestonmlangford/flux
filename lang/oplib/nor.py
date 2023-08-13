
decl_u = """
u$ u$_nor(size_t argc, u$ argv[]);
"""

impl_u = """
u$ u$_nor(size_t argc, u$ argv[])
{
    u$ result = {};
    uint$_t sum = UINT$_MAX;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                sum = sum | argv[i].value;
            }
        }
    }

    if (okay)
    {
        result.value = ~sum;
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
boolean boolean_nor(size_t argc, boolean argv[]);
"""

impl_b = """
boolean boolean_nor(size_t argc, boolean argv[])
{
    boolean result = {};
    bool sum = true;
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            okay = okay && argv[i].valid;

            if (okay)
            {
                sum = sum || argv[i].value;
            }
        }
    }

    if (okay)
    {
        result.value = !sum;
        result.valid = true;
    }

    return result;
}
"""
