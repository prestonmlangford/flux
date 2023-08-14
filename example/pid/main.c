#include <stdio.h>
#include "unistd.h"
#include "flux.h"
#include "pid.h"

int main()
{
    struct Pid pid =
    {
        .reset = TRUE,
        .Kp = I32(-1),
        .Ki = I32(1),
        .Kd = I32(1),
        .r = I32(1000),
        .y = I32(0)
    };
    int i = 0;

    module_pid(&pid);
    pid.reset = FALSE;

    for (i = 0; i < 30; i++)
    {
        pid.y.value = pid.u.value/2;
        module_pid(&pid);
        printf("%d %s\n",pid.y.value,pid.u.valid ? "valid" : "invalid");
    }

    return 0;
}