import sys
import urllib.request
download = ''
package = sys.argv[1]
dest = sys.argv[2]
download = 'https://github.com/sap-ai/pimpstore/' + package
urllib.request.urlretrieve(download, dest)
