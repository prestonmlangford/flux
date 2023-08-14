#ifndef MUX_H
#define MUX_H

u8 u8_mux(boolean s, u8 a, u8 b);

i8 i8_mux(boolean s, i8 a, i8 b);

u16 u16_mux(boolean s, u16 a, u16 b);

i16 i16_mux(boolean s, i16 a, i16 b);

u32 u32_mux(boolean s, u32 a, u32 b);

i32 i32_mux(boolean s, i32 a, i32 b);

u64 u64_mux(boolean s, u64 a, u64 b);

i64 i64_mux(boolean s, i64 a, i64 b);

boolean boolean_and(size_t argc, boolean argv[]);

#endif /* MUX_H */
