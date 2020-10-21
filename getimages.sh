while true
do
  FILE=`date +%Y%m%d/%H00/%Y%m%d%H%M%S.jpg`
  DIR=`dirname ${FILE}`
  echo "${FILE} ${DIR}"
  mkdir -p $DIR
  raspistill -o ${FILE}
  sleep 60
done
