import random
import tls_client
from log import Logger
import base64
import json
import urllib
import time

log = Logger("CSolver")

class CSolver:
    def __init__(self, site, key):
        self.key = key
        try: 
            self.domain = site.split("://")[1].split("/")[0]
        except:
            self.domain = site
        if 'http' not in site:
            self.site = f'https://{site}/'
        else:
            self.site = site
        self.client = tls_client.Session(random_tls_extension_order=True, client_identifier="chrome_130")
        self.client.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': self.site,
            'priority': 'u=1, i',
            'referer': self.site,
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        
    def payload(self):
        with open('payload.json', 'r') as f:
            payload = json.load(f)
            
        payload['cokys'] = base64.b64encode('loadTimescsiapp,'.encode()).decode()
        payload['cfpfe'] = base64.b64encode('Error: Cannot read properties of null'.encode()).decode()
        payload['stcfp'] = base64.b64encode('.com/pa/js/min/pa.js:2:6832)\n    at https://www.paypalobjects.com/pa/js/min/pa.js:2:54812\n    at https://www.paypalobjects.com/pa/js/min/pa.js:2:70132'.encode()).decode()
        payload['dcok'] = f".{self.domain}"
        
        return payload
            
    def mouse(self):
        mm = {
            "mousemove":random.randint(30,185),
            "click":0,
            "scroll":0,
            "touchstart":0,
            "touchend":0,
            "touchmove":0,
            "keydown":0,
            "keyup":0
        }
        
        return mm
            
    def data(self):
        # Eh, might make dynamnic if i get bored enuf 
        return 'guKlxLs31MgajRm9nSqtWsvytRrRVmIri9iXPnTWg9GkVs0eDz_u0TRlB5wwHoegKYxblgYYAfILhVIAyV4QPDM9vRim4tCJRaPFOMBW0cWQ6U604AxTGbCmB2oBrM7l'
            
    def datadome(self):
        st = time.time()
        data = self.data()
        jsData = self.payload()
        eventCounters = self.mouse()
        cid = data
        ddk = self.key
        Referer = urllib.parse.quote(self.site)
        request = urllib.parse.quote(self.site.split("://")[1].split('/')[1])
        
        payload = {
            'jsData': jsData,
            'eventCounters': eventCounters,
            'jsType': 'le',
            'cid': cid,
            'ddk': ddk,
            'Referer': Referer,
            'request': request,
            'responsePage': 'origin',
            'ddv': '4.35.4'
        }
        
        r = self.client.post(f"https://ddbm2.{self.domain}/js/", data=payload)
        token = r.json()['cookie'].split(';')[0]
        log.success(f"Solved Datadome -> {token[:50]}... -> {round(time.time()-st, 2)}s")
        
while True:
    CSolver("https://paypal.com/signin", "C992DCAFEE25FA95C6492C61EB3328").datadome()