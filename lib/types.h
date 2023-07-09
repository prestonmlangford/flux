#ifndef TYPES_H
#define TYPES_H

#include <stdlib.h>

#define CONST(x) {.value = (x), .valid = true}

typedef enum {false,true} bool;

#define SIGNAL(name,ctype) typedef struct name {ctype value;bool valid;} name

SIGNAL(i64, int64_t);
SIGNAL(u64,uint64_t);
SIGNAL(i32, int32_t);
SIGNAL(u32,uint32_t);
SIGNAL(i16, int16_t);
SIGNAL(u16,uint16_t);
SIGNAL( i8,  int8_t);
SIGNAL( u8, uint8_t);

SIGNAL(f32, float);
SIGNAL(f64, double);

SIGNAL(boolean, bool);



#endif /* TYPES_H */
