#!/bin/bash
set -o nounset -o errexit
export ZEPPELIN_PORT=${ContainerRunProcessConstants.PublishedInternalPort};
export ZEPPELIN_NOTEBOOK_DIR=$ZeppelinRoot/notebooks;
export ZEPPELIN_LOG_DIR=$ZeppelinRoot/log;
if [ -z ${DOMINO_SPARK_CONFIG_MASTER+x} ]; then
echo "DOMINO_SPARK_CONFIG_MASTER not set";
  else export MASTER=$DOMINO_SPARK_CONFIG_MASTER
fi
/opt/zeppelin/bin/zeppelin.sh