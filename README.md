# door
Street door software

Uses a RPI3 and hyperion relay board like hp-arl-2ch5v

The relay board is connected to the 5V, gpio 18 and ground of RPI3.

The contact of the relay (output) are connected in parallel with the button that opens the street door.
To open the door:
```
/usr/bin/gpioset -m time -s 1 gpiochip0 18=1
```


The httpd.conf (/etc/httpd/conf/httpd.conf) needs the following add (change 10.0.0.201 by our RPI3 address):
I have done the same in conf.d/ssl.conf ...
```
# Send any page to index.html
rewriteengine on
rewritecond %{request_uri} !^/index.html
rewritecond %{request_uri} !^/door.html
rewritecond %{request_uri} !^/cgi-bin
rewritecond %{request_uri} !^/generate_204
rewriterule ^. http://10.0.0.201/index.html [R,L]
# rewriterule ^. /index.html [R,L]

<FilesMatch "door">
  AuthName "Member Only"
  AuthType Basic
  AuthUserFile /etc/httpd/conf/htpasswd
  require valid-user
</FilesMatch>
```

And some cgi activation...
alias_module one:
```
ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"
```
permission to read etc:
```
<Directory "/var/www/cgi-bin">
    AllowOverride None
    Options None
    Require all granted
</Directory>
```
mime_module one:
```
AddHandler cgi-script .cgi
```
For the 204 response:
```
ErrorDocument 404 "/cgi-bin/missing_handler.cgi"
```

Quick install:
```bash
cd door
cp -p html/* /var/www/html/
cp -p cgi-bin/* /var/www/cgi-bin
```
