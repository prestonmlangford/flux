#include "pid.h"

#define I32_ZERO I32(0)

static i32 eval_i(struct Pid* self);
static i32 eval_u_1(struct Pid* self);
static i32 eval_u_2(struct Pid* self);
static i32 eval_u_3(struct Pid* self);
static i32 eval_u(struct Pid* self);

static i32 eval_i(struct Pid* self)
{
    i32 argv[] =
    {
        self->e,
        self->i_prev,
    };
    size_t argc = LEN(argv);

    return i32_sum(argc, argv);
}

static i32 eval_u_1(struct Pid* self)
{
    i32 argv[] =
    {
        self->Kp,
        self->e,
    };
    size_t argc = LEN(argv);

    return i32_mul(argc, argv);
}

static i32 eval_u_2(struct Pid* self)
{
    i32 argv[] =
    {
        self->Ki,
        self->i,
    };
    size_t argc = LEN(argv);

    return i32_mul(argc, argv);
}

static i32 eval_u_3(struct Pid* self)
{
    i32 argv[] =
    {
        self->Kd,
        self->d,
    };
    size_t argc = LEN(argv);

    return i32_mul(argc, argv);
}

static i32 eval_u(struct Pid* self)
{
    i32 argv[] =
    {
        eval_u_1(self),
        eval_u_2(self),
        eval_u_3(self),
    };
    size_t argc = LEN(argv);

    return i32_sum(argc, argv);
}

void module_pid(struct Pid* self)
{
    self->e = i32_sub(self->r,self->y);
    self->i = eval_i(self);
    self->d = i32_sub(self->e,self->e_prev);
    self->i_prev = i32_mux(self->reset,I32_ZERO,self->i);
    self->e_prev = self->e;
    self->u = eval_u(self);
}

