#!/usr/bin/env python

import requests
import sys
import json

def main(token):
    response = requests.get("https://webhook.site/token/{}/requests?page=0".format(token))
    response.raise_for_status()
    for wh in response.json()['data']:
        data = wh['content']
        if data != "":
            print "DNAC:{}".format(wh['ip'])
            print json.dumps(json.loads(data), indent=2)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        token="475e0feb-c5ac-4e64-b685-e6aaf8b4ccf2"
    else:
        token = sys.argv[1]
    main(token)