INC=
INC+=" -Iblocks"
INC+=" -Isheets"
INC+=" -I."

SRC=
SRC+=" blocks/debounce.c"
SRC+=" blocks/edge.c"
SRC+=" blocks/and.c"
SRC+=" sheets/landing.c"
SRC+=" main.c"

gcc $INC $SRC