#ifndef TYPES_H
#define TYPES_H

#include <stdlib.h>

typedef enum {false,true} bool;

#define SIGNAL_DECL(name,ctype) typedef struct name {ctype value;bool valid;} name

SIGNAL_DECL(i64, int64_t);
SIGNAL_DECL(u64,uint64_t);
SIGNAL_DECL(i32, int32_t);
SIGNAL_DECL(u32,uint32_t);
SIGNAL_DECL(i16, int16_t);
SIGNAL_DECL(u16,uint16_t);
SIGNAL_DECL( i8,  int8_t);
SIGNAL_DECL( u8, uint8_t);

SIGNAL_DECL(f32, float);
SIGNAL_DECL(f64, double);

SIGNAL_DECL(boolean, bool);

#define SIGNAL_INIT(x) {.value = (x), .valid = true}

#define I64(x) ((i64) SIGNAL_INIT(x))
#define U64(x) ((u64) SIGNAL_INIT(x))
#define I32(x) ((i32) SIGNAL_INIT(x))
#define U32(x) ((u32) SIGNAL_INIT(x))
#define I16(x) ((i16) SIGNAL_INIT(x))
#define U16(x) ((u16) SIGNAL_INIT(x))
#define  I8(x) (( i8) SIGNAL_INIT(x))
#define  U8(x) (( u8) SIGNAL_INIT(x))

#define F64(x) ((f64) SIGNAL_INIT(x))
#define F32(x) ((f32) SIGNAL_INIT(x))

#define  TRUE ((boolean) SIGNAL_INIT(true))
#define FALSE ((boolean) SIGNAL_INIT(false))

#endif /* TYPES_H */
