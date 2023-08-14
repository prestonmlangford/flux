
impl Pid
{
    in boolean reset;
    in i32 r;
    in i32 y;
    in i32 Kp;
    in i32 Ki;
    in i32 Kd;
    
    const i32 I32_ZERO = 0;
    
    var i32 e = sub(r,y);
    var i32 i = sum(e,i_prev);
    var i32 d = sub(e,e_prev);

    var i32 i_prev = mux(reset,I32_ZERO,i);
    var i32 e_prev = e;
    
    out i32 u = sum(
        mul(Kp,e),
        mul(Ki,i),
        mul(Kd,d)
    );
};
