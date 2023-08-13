
decl_u = """
u$ u$_mul(size_t argc, u$ argv[]);
"""

impl_u = """
u$ u$_mul(size_t argc, u$ argv[])
{
    u$ result = {};
    uint$_t product = UINT$_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            uint$_t a = product;
            uint$_t b = argv[i].value;

            okay = okay && argv[i].valid;

            if (b > UINT$_C(0))
            {
                int$_t limit = UINT$_MAX / b;
                okay = okay && (a <= limit);
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}
"""

decl_i = """
i$ i$_mul(size_t argc, i$ argv[]);
"""

impl_i = """
i$ i$_mul(size_t argc, i$ argv[])
{
    i$ result = {};
    int$_t product = INT$_C(1);
    bool okay = (argc > 1U) && (argv != NULL);
    size_t i = 0U;

    if (okay)
    {
        for (i = 0U; i < argc; i++)
        {
            int$_t a = product;
            int$_t b = argv[i].value;
            bool a_pos = a > INT$_C(0);
            bool b_pos = b > INT$_C(0);

            okay = okay && argv[i].valid;

            if (a_pos)
            {
                if (b_pos)
                {
                    int$_t limit = INT$_MAX / b;
                    okay = okay && (a <= limit);
                }
                else
                {
                    int$_t limit = INT$_MIN / a;
                    okay = okay && (b >= limit);
                }
            }
            else
            {
                if (b_pos)
                {
                    int$_t limit = INT$_MIN / b;
                    okay = okay && (a >= limit);
                }
                else if (a != INT$_C(0))
                {
                    int$_t limit = INT$_MAX / a;
                    okay = okay && (b >= limit);
                }
            }

            if (okay)
            {
                product = a * b;
            }
        }
    }

    if (okay)
    {
        result.value = product;
        result.valid = true;
    }

    return result;
}
"""

decl_f = ""
impl_f = ""

decl_b = ""
impl_b = ""
