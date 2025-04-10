import sys
import requests
from bs4 import BeautifulSoup
dest = sys.argv[1]
package = 'https://github.com/sap-ai/pimpstore/blob/main/' + dest
fl = requests.get(package)
soup = BeautifulSoup(fl.content, 'html.parser')
d = soup.find('textarea')
with open(dest, 'w') as file:
    file.write(d)
