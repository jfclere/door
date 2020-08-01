#!/usr/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
echo '<title>Welcome Home</title>'
echo '</head>'
echo '<body>'
read a < /tmp/status.txt
echo "Hello the blinds button is ${a} now...<br/>"
echo "What do you want to do:"
echo "<p><a href=\"/cgi-bin/blinds.cgi?DARK\"> Get less light</a></p>"
echo "<p><a href=\"/cgi-bin/blinds.cgi?LIGHT\"> Get more light</a></p>"
echo "<p><a href=\"/cgi-bin/blinds.cgi?UP\"> Get the blinds up completly</a></p>"
echo "<p><a href=\"/cgi-bin/blinds.cgi?DOWN\"> Get the blinds down completly</a></p>"
if [ ! -z ${QUERY_STRING} ];then
  echo ${QUERY_STRING} > /tmp/cmd.txt
  echo "Doing ${QUERY_STRING} be patient"
fi
echo '</body>'
echo '</html>'

exit 0
