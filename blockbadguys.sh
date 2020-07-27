journalctl -b 0 -u sshd | grep "Failed password for" > /tmp/$$.tmp.1
cat /tmp/$$.tmp.1 | grep "invalid user" | awk '{ print $13 }' > /tmp/$$.tmp
cat /tmp/$$.tmp.1 | grep -v "invalid user" | awk '{ print $11 }' >> /tmp/$$.tmp
sort -u /tmp/$$.tmp > /tmp/$$.tmp.2
while read a
do
  echo "firewall-cmd --permanent --zone=FedoraServer  --add-rich-rule=\"rule family='ipv4' source address='"$a"' reject\""
done < /tmp/$$.tmp.2
