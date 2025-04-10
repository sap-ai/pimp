import sys
import requests
from bs4 import BeautifulSoup
dest = sys.argv[1]
package = 'https://github.com/sap-ai/pimpstore/blob/main/' + dest
fl = requests.get(package)
soup = BeautifulSoup(fl.content, 'html.parser')
d = soup.find('textarea')
li = []
s = ""
fnl = ""
for link in soup.find_all('textarea'):
   try:
      li = link.split(">")
      s = ''.join(li)
      li = s.split("<")
      s = ''.j(li)
       try:
         exec(s)
         fnl = li[0]
      except:
         pass
with open(dest, 'w') as file:
   file.write(str(fnl))
