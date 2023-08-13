
decl_u = """
u$ u$_sum(size_t argc, u$ argv[]);
"""

impl_u = """
u$ u$_sum(size_t argc, u$ argv[])
{
    u$ result = {};
    uint$_t sum = UINT$_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint$_t term = argv[i].value;
            uint$_t limit = UINT$_MAX - term;

            okay = okay && argv[i].valid;
            okay = okay && (sum <= limit);

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}
"""

decl_i = """
i$ i$_sum(size_t argc, i$ argv[]);
"""

impl_i = """
i$ i$_sum(size_t argc, i$ argv[])
{
    i$ result = {};
    int$_t sum = INT$_C(0);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;
    
    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int$_t term = argv[i].value;
            okay = okay && argv[i].valid;
            
            if (term > INT$_C(0))
            {
                int$_t limit = INT$_MAX - term;
                okay = okay && (sum <= limit);
            }
            else if (term < INT$_C(0))
            {
                int$_t limit = INT$_MIN - term;
                okay = okay && (sum >= limit);
            }
            else
            {
                /* Do nothing. */
            }

            if (okay)
            {
                sum = sum + term;
            }
        }
    }

    if (okay)
    {
        result.value = sum;
        result.valid = true;
    }
    
    return result;
}
"""

decl_f = ""
impl_f = ""

decl_b = ""
impl_b = ""
