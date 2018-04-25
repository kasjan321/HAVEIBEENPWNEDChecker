##Created by kasjan321
import urllib3
import sys
import requests
import argparse
pwned = None 
safe = "SAFE"
pwned = "PWNED"
parser = argparse.ArgumentParser()
parser.add_argument("email")
args = parser.parse_args()
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
http = urllib3.PoolManager(10, headers=user_agent)
request = http.request('GET', 'https://haveibeenpwned.com/api/v2/breachedaccount/' + args.email)
output = request.data.decode('utf-8')
sys.stdout.write("\033[0;32m")
if len(output) <= 1: print(safe)
sys.stdout.write("\033[1;31m")
if len(output) >= 1: print(pwned)

 

