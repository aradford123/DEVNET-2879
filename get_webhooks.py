#!/usr/bin/env python

import requests
import sys
import json

def main(token):
    response = requests.get("https://webhook.site/token/{}/requests?page=0".format(token))
    response.raise_for_status()
    print response.json()
    for wh in response.json()['data']:
        data = wh['content']
        if data != "":
            print "DNAC:{}".format(wh['ip'])
            print json.dumps(json.loads(data), indent=2)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # default webhook test
        token="927d59d5-f0f4-4155-a7d7-00718b33d74d"
    else:
        token = sys.argv[1]
    main(token)
