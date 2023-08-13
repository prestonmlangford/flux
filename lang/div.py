"""

            01 | 10
            11 | 11
            -------
            01 | 10
       00 | 11
       01 | 10
  00 | 11
---------------------
  01 | 01 | 10 | 10

"""

def mul(a,b,w):
    s = w // 2
    m = (1 << s) - 1
    a0 = a & m
    a1 = a >> s
    b0 = b & m
    b1 = b >> s

    p00 = a0 * b0
    p01 = a0 * b1
    p10 = a1 * b0
    p11 = a1 * b1

    p000 = p00 & m
    p001 = p00 >> s
    p010 = p01 & m
    p011 = p01 >> s
    p100 = p10 & m
    p101 = p10 >> s
    p110 = p11 & m
    p111 = p11 >> s
    
    l = p000
    ml = p001 + p010 + p100
    c = ml >> s
    mu = c + p011 + p101 + p110
    c = mu >> s
    u = c + p111
    
    lower  = ((ml & m) << s) + l
    upper  = (u << s) + (mu >> s)

    print(f"s {s}")
    print(f"m {m}")
    print(f"a0 {a0}")
    print(f"a1 {a1}")
    print(f"b0 {b0}")
    print(f"b1 {b1}")
    print(f"p00 {p00}")
    print(f"p01 {p01}")
    print(f"p10 {p10}")
    print(f"p11 {p11}")
    print(f"l {l}")
    print(f"ml {ml}")
    print(f"mu {mu}")
    print(f"u {u}")
    print(f"lower {lower}")
    print(f"upper {upper}")

    return (upper << w) | lower

    
def div(a,b):
    if a < b:
        return 0,a
    else:
        q = 0
        r = a
        
        while True:
            q = q + 1
            r = r - b
            if r < b:
                break
        
        return q,r
    

print(mul(100,6,8))