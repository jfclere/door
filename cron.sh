#!/bin/bash
/usr/bin/ping -c 1 -W 10 www.apache.org
if [ $? -eq 0 ]; then
  exit 0
fi

/usr/bin/ping -c 1 -W 10 google.com
if [ $? -eq 0 ]; then
  exit 0
fi

/usr/bin/echo "No Internet!!!" > /root/`/usr/bin/date +%F.%H.%M`

/usr/bin/ping -c 1 -W 10 192.168.1.1
if [ $? -eq 0 ]; then
  exit 0
fi

/usr/bin/dmesg > /root/`/usr/bin/date +%F.%H.%M`

/usr/bin/dmesg | /usr/bin/grep "mailbox indicates firmware halted"
if [ $? -eq 0 ]; then
  /usr/bin/sync
  /usr/bin/sleep 10
  /usr/sbin/reboot
fi
