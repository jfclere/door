# door
Street door software

Uses a RPI3 and hyperion relay board like hp-arl-2ch5v (most are using: SRD-05VDC-SL-C)

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
mime_module one (commented out):
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
in the sudoers:
```
apache ALL=NOPASSWD: /usr/bin/gpioset -m time -s 1 gpiochip0 18=1
```
in /etc/passwd: /sbin/nologin (only for testing -> /bin/bash)
```
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
```

# Blinds
Software to get the blinds up/down via RPI3.
Use 32 bits fedora (64 doesn't work with python3-RPi.GPIO)
```
yum install python3-RPi.GPIO
```
in  /boot/extlinux/extlinux.conf append to the kernel configuration:
```
iomem=relaxed
```

# firewall commands to prevent ssh login tries that slow down the RPI3
```
firewall-cmd --permanent --zone=FedoraServer  --add-rich-rule="rule family='ipv4' source address='111.161.74.113' reject"
firewall-cmd --permanent --zone=FedoraServer  --add-rich-rule="rule family='ipv4' source address='222.186.173.226' reject"
firewall-cmd --permanent --zone=FedoraServer  --add-rich-rule="rule family='ipv4' source address='111.30.114.22' reject"
firewall-cmd --reload
```

# raspios install
```bash
apt-get install gpiod
apt-get install apache2
apt-get install libapache2-mod-md
mkdir -p /var/www/cgi-bin
a2enmod cgid
a2enmod rewrite
systemctl restart apache2
```

file "moved":
/etc/httpd/conf/httpd.conf to /etc/apache2/apache2.conf

/var/log/apache2 for logs and errors...

/var/www/cgi-bin/ to /usr/lib/cgi-bin/

/etc/apache2/conf-enabled/serve-cgi-bin.conf make to change to /var/www/cgi-bin/

install the service:
```bash
cp blinds.service /etc/systemd/system/
sudo systemctl enable blinds
```
 
