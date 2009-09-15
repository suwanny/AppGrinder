#!/bin/bash
GRINDERPATH=/home/spark/Project/Grinder/grinder
export GRINDERPROPERTIES=${GRINDERPATH}/bin/grinder.properties
echo ${GRINDERPROPERTIES}

CLASSPATH="/usr/lib/jvm/java-6-sun/lib/rt.jar"
for file in $GRINDERPATH/lib/*.jar;
do
  CLASSPATH=$CLASSPATH:$file
done

#export CLASSPATH=$GRINDERPATH/lib/grinder.jar:$CLASSPATH
echo ${CLASSPATH}

export JAVA_HOME=/usr/lib/jvm/java-6-sun
export PATH=$JAVA_HOME/bin:$PATH
#export ${CLASSPATH} ${PATH} ${GRINDERPROPERTIES}
