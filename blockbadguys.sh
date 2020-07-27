#journalctl -xe | grep "Invalid user" | awk '{ print $10 }' | sort -u | awk '{ print "firewall-cmd --permanent --zone=FedoraServer  --add-rich-rule=\"rule family='ipv4' source address='" $0 "' reject\"" }'
journalctl -xe | grep "Invalid user" | awk '{ print $10 }' | sort -u > /tmp/$$.tmp
while read a
do
  echo "firewall-cmd --permanent --zone=FedoraServer  --add-rich-rule=\"rule family='ipv4' source address='"$a"' reject\""
done < /tmp/$$.tmp
