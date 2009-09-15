#!/bin/bash
# Start Console
#
GRINDERPATH=/home/spark/Project/Grinder/grinder
${GRINDERPATH}/bin/setGrinderEnv.sh

java -cp $CLASSPATH net.grinder.Console
