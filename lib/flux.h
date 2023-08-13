#ifndef TYPES_H
#define TYPES_H

#include <stdlib.h>
#include <stdint.h>

#define LEN(arr) (sizeof(arr)/sizeof(arr[0]))

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

#define VALID(x) {.value = x, .valid = true}
#define SIGNAL_LITERAL(type,x) ((type) VALID(x))

#define I64(x) SIGNAL_LITERAL(i64, INT64_C(x))
#define U64(x) SIGNAL_LITERAL(u64,UINT64_C(x))
#define I32(x) SIGNAL_LITERAL(i32, INT32_C(x))
#define U32(x) SIGNAL_LITERAL(u32,UINT32_C(x))
#define I16(x) SIGNAL_LITERAL(i16, INT16_C(x))
#define U16(x) SIGNAL_LITERAL(u16,UINT16_C(x))
#define  I8(x) SIGNAL_LITERAL( i8,  INT8_C(x))
#define  U8(x) SIGNAL_LITERAL( u8, UINT8_C(x))

#define F64(x) SIGNAL_LITERAL(f64,x)
#define F32(x) SIGNAL_LITERAL(f32,x)

#define  TRUE SIGNAL_LITERAL(boolean, true)
#define FALSE SIGNAL_LITERAL(boolean, false)

#define SIGNAL_INVALID(type) ((type) {})

#define I64_INVALID SIGNAL_INVALID(i64)
#define U64_INVALID SIGNAL_INVALID(u64)
#define I32_INVALID SIGNAL_INVALID(i32)
#define U32_INVALID SIGNAL_INVALID(u32)
#define I16_INVALID SIGNAL_INVALID(i16)
#define U16_INVALID SIGNAL_INVALID(u16)
#define  I8_INVALID SIGNAL_INVALID( i8)
#define  U8_INVALID SIGNAL_INVALID( u8)

#define F64_INVALID SIGNAL_LITERAL(f64)
#define F32_INVALID SIGNAL_LITERAL(f32)

#define BOOLEAN_INVALID SIGNAL_LITERAL(boolean)
#define IS_TRUE(b) (b.value && b.valid)

#include "ops/lte.h"
#include "ops/neg.h"
#include "ops/div.h"
#include "ops/nor.h"
#include "ops/or.h"
#include "ops/gt.h"
#include "ops/gte.h"
#include "ops/eq.h"
#include "ops/neq.h"
#include "ops/lt.h"
#include "ops/not.h"
#include "ops/mul.h"
#include "ops/sub.h"
#include "ops/xor.h"
#include "ops/sum.h"
#include "ops/rem.h"
#include "ops/xnor.h"
#include "ops/nand.h"
#include "ops/and.h"

#endif /* TYPES_H */
