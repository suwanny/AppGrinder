#!/bin/bash
# Start Agent 
#
GRINDERPATH=/home/spark/Project/Grinder/grinder
GRINDERPROPERTIES=${GRINDERPATH}/bin/agent.properties

CLASSPATH="/usr/lib/jvm/java-6-sun/lib/rt.jar"
for file in $GRINDERPATH/lib/*.jar;
do
  CLASSPATH=$CLASSPATH:$file
done

export JAVA_HOME=/usr/lib/jvm/java-6-sun
export PATH=$JAVA_HOME/bin:$PATH

java -cp $CLASSPATH net.grinder.Grinder $GRINDERPROPERTIES
