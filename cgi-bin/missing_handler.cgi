#!/usr/bin/bash

if [ "$REQUEST_URI" == "/generate_204" ]; then
    echo "Status: 204 No Content"
    echo ""
    exit
fi

echo "Status: 404 Not Found"
echo "Content-Type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Thanks Welcome Home</title>'
echo '</head>'
echo '<body>'
echo 'Not FOUND'
echo '</body>'
echo '</html>'

exit 0
