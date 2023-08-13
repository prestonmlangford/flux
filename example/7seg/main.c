#include <stdio.h>
#include "flux.h"
#include "seg7.h"


/*
 _         _    _         _    _    _    _    _ 
| |    |   _|   _|  |_|  |_   |_     |  |_|  |_|
|_|.   |. |_.   _|.   |.  _|. |_|.   |. |_|.  _|.

_1_n
234n
567.n

*/

void display(bool seg[7])
{
    char str[16] = 
    {
         [0]=' ',
         [1]=seg[0] ? '_' : ' ',
         [2]=' ',
         [3]='\n',
         [4]=seg[1] ? '|' : ' ',
         [5]=seg[2] ? '_' : ' ',
         [6]=seg[3] ? '|' : ' ',
         [7]='\n',
         [8]=seg[4] ? '|' : ' ',
         [9]=seg[5] ? '_' : ' ',
        [10]=seg[6] ? '|' : ' ',
        [11]='.',
        [12]='\n',
        [13]='\0',
        [14]='\0',
        [15]='\0',
    };

    printf("%s",str);
}

int main()
{
    struct Seg7 seg7 = 
    {
        .reset = TRUE,
    };
    bool segments[7] = {};

    while (1)
    {
        module_seg7(&seg7);
        seg7.reset = FALSE;

        segments[0] = IS_TRUE(seg7.top);
        segments[1] = IS_TRUE(seg7.topl);
        segments[2] = IS_TRUE(seg7.mid);
        segments[3] = IS_TRUE(seg7.topr);
        segments[4] = IS_TRUE(seg7.botl);
        segments[5] = IS_TRUE(seg7.bot);
        segments[6] = IS_TRUE(seg7.botr);
        
        if (IS_TRUE(seg7.refresh))
        {
            display(segments);
        }
    }

    return 0;
}