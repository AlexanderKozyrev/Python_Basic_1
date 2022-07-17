import requests
import re


url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url).text
pattern = r'<h3.*>(.*)</h3>'
result = re.findall(pattern, response)
print(result)
