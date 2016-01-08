#!/bin/bash
set -e

cd /pin/source/tools/mica/

if [ "$RECOMPILE" = true ] ; then
  make
fi

# delete any previous output
rm -f *.out

# execute pre-tasks
if [ -n "$PRE" ] ; then
  exec $PRE
fi

# analyze main task
LD_LIBRARY_PATH=`pwd` ../../../pin \
  -follow_execv \
  -t mica.so -- sh -c "$CMD"

# copy generated output
find / -name *pin.out | xargs cp -t . || true
