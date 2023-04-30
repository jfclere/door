#!/usr/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
echo '<title>Thanks processing request</title>'
echo '</head>'
echo '<body>'
read a < /tmp/status.txt
echo "Hello the blinds button is ${a} now..."
echo "Doing ${QUERY_STRING} be patient..."
echo ${QUERY_STRING} > /tmp/cmd.txt
echo '</body>'
echo '</html>'

exit 0
