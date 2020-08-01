#!/usr/bin/bash

echo "Content-type: text/html"
echo ""

#/usr/bin/gpioinfo

#sudo /usr/bin/gpioset -m time -s 1 gpiochip0 18=1

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
echo '<title>Thanks Welcome Home</title>'
echo '</head>'
echo '<body>'
echo 'Hello use the NUKI webapp for the door...'
echo "<p><a href=\"/cgi-bin/blinds.cgi\"> Play with the blinds</a></p>"
echo '</body>'
echo '</html>'

exit 0
