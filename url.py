# uploading website content
import json
from urllib.request import urlopen


with urlopen("http://g.co/dev/maps-no-account") \
as response:
	source = response.read()
	print(source)
