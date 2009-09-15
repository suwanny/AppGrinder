#!/bin/bash
# Start Proxy
#

GRINDERPATH=/home/spark/Project/Grinder/grinder

CLASSPATH="/usr/lib/jvm/java-6-sun/lib/rt.jar"
for file in $GRINDERPATH/lib/*.jar;
do
  CLASSPATH=$CLASSPATH:$file
done

export JAVA_HOME=/usr/lib/jvm/java-6-sun
export PATH=$JAVA_HOME/bin:$PATH

SCRIPT_NAME="test_script" 
if [ "$1" != "" ]
then 
	SCRIPT_NAME=$1
fi

PROXY_OPTION="-http"
#PROXY_OPTION=${PROXY_OPTION}" -console"
PROXY_OPTION=${PROXY_OPTION}" -localhost twolves.cs.ucsb.edu"
PROXY_OPTION=${PROXY_OPTION}" -localport 8008"

#echo ${SCRIPT_NAME}.py
CMD="java -cp ${CLASSPATH} net.grinder.TCPProxy ${PROXY_OPTION} > ${SCRIPT_NAME}.py"
echo ${CMD}
#${CMD}
java -cp ${CLASSPATH} net.grinder.TCPProxy ${PROXY_OPTION} > ${SCRIPT_NAME}.py


