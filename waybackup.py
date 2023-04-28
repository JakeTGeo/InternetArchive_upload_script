#! /usr/bin/env python3

import sys, requests
import time
# Usage: Pass URL to script, get back URL to Wayback Machine snapshot
 
base_url = 'http://web.archive.org'

lines_work = [] # enter list of links to save

counter = 0
for item in lines_work:
    r = requests.get(base_url + '/save/' + lines_work[counter].strip("\n"))
    if r.status_code == requests.codes.ok:
        to_be_parsed = (base_url + r.headers['link'])
        x = (to_be_parsed.split())
        print(x[5])
        time.sleep(15)
        counter += 1
    else:
       print('Error in response: ' + str(r.status_code) + lines_work[counter])
#   or you could just return the original url
# print sys.argv[1]
 
 
 

