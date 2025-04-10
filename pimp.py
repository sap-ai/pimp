import sys
import requests
from bs4 import BeautifulSoup
dest = sys.argv[1]
package = 'https://github.com/sap-ai/pimpstore/blob/main/' + dest
download_large_file(package, dest)
fl = requests.get(url)
soup = BeautifulSoup(fl, 'html.parser')
d = soup.find('textarea')
with open(dest, 'w') as file:
    file.write(d)
