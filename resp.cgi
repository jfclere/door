#!/usr/bin/bash
echo "Status: 200 OK"
echo "Content-Type: application/ocsp-response"
echo "Content-Length: 21"
echo "last-modified: Wed 16 May 18:41:56 CEST 2018"
echo "ETag: EXXLKD:LS"
echo "expires: Wed 16 May 18:41:56 CEST 2019"
echo "cache-control: public"
echo "date: Wed 16 May 18:41:56 CEST 2018"
echo ""
cat /home/jfclere/TMP/JWS-971/resp_revoked_first.out
