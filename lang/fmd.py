"""
FP61_FORCE_INLINE uint64_t Emulate64x64to128(
    uint64_t& r_hi,
    const uint64_t x,
    const uint64_t y)
{
    const uint64_t x0 = (uint32_t)x, x1 = x >> 32;
    const uint64_t y0 = (uint32_t)y, y1 = y >> 32;
    const uint64_t p11 = x1 * y1, p01 = x0 * y1;
    const uint64_t p10 = x1 * y0, p00 = x0 * y0;
    /*
        This is implementing schoolbook multiplication:

                x1 x0
        X       y1 y0
        -------------
                   00  LOW PART
        -------------
                00
             10 10     MIDDLE PART
        +       01
        -------------
             01 
        + 11 11        HIGH PART
        -------------
    */

    // 64-bit product + two 32-bit values
    const uint64_t middle = p10 + (p00 >> 32) + (uint32_t)p01;

    // 64-bit product + two 32-bit values
    r_hi = p11 + (middle >> 32) + (p01 >> 32);

    // Add LOW PART and lower half of MIDDLE PART
    return (middle << 32) | (uint32_t)p00;
}

"""


"""

N / D => Q, R

where N = (Q * D) + R

X * N = (X * Q * D) + (X * R)
X * N / D = (X * Q) + ((X * R) / D)

X * N / D => X * Q, X * R

"""

"""
This is implementing schoolbook multiplication:

        x1 x0
X       y1 y0
-------------
            00  LOW PART
-------------
        00
        10 10     MIDDLE PART
+       01
-------------
        01 
+ 11 11        HIGH PART
-------------


        x1 x0
X       y1 y0
-------------
        01 00  LOW PART
-------------
     11 10


"""

decl_u = """
u$ u$_fmd(u$ x, u$ a, u$ b);
"""

impl_u = """
u$ u$_fmd(u$ a, u$ b)
{
    u$ result = {};
    bool divide_by_zero = b.value == INT$_C(0);

    if (a.valid && b.valid && (!divide_by_zero))
    {
        uint$_t m = x.value;
        uint$_t q = a.value / b.value;
        uint$_t r = a.value % b.value;
        
        // a / b => q, r
        // a = (b * q) + r
        // m * a = (m * b * q) + (m * r)
        // m * a / b = (m * q) + ((m * r) / b)

        if (b > UINT$_C(0))
        {
            int$_t limit = UINT$_MAX / b;
            okay = okay && (a <= limit);
        }
        
        result.value = PMLFIXME;
        result.valid = true;
    }

    return result;
}
"""

decl_i = """
i$ i$_fmd(i$ a, i$ b);
"""

impl_i = """
i$ i$_fmd(i$ a, i$ b)
{
    i$ result = {};
    bool divide_by_zero = b.value == INT$_C(0);
    bool overflow = (a.value == INT$_MIN) && (b.value == INT$_C(-1));

    if (a.valid && b.valid && (!overflow) && (!divide_by_zero))
    {
        result.value = a.value / b.value;
        result.valid = true;
    }

    return result;
}
"""

decl_f = ""
impl_f = ""

decl_b = ""
impl_b = ""
