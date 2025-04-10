import sys
import requests
def download_large_file(url, destination):
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(destination, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("Package downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print("Error downloading the Package:", e)
dest = sys.argv[1]
package = 'https://github.com/sap-ai/pimpstore/' + dest
download_large_file(package, dest)
