#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Script to generate a QR Code for a WiFi SSID. 
# Based on WiFi QRCode string from
#   https://en.wikipedia.org/wiki/QR_code#Joining_a_Wi%E2%80%91Fi_network
#
# Usage:
#   qr_wifi.py > qr.html
# -----------------------------------------------------------------------------

import qrcode

type = 'WPA2'       # T: Authentication Type (WEP, WPA, WPA2, nopass, or blank)
ssid = 'Guest'      # S: SSID; optionally in double-quotes
passwd = 'LetMeIn!' # P: Password; optionally in double-quotes
hidden = 'false'    # H: Hidden SSID? true or false
qr_string = 'WIFI:T:{T};S:{S};P:{P};H:{H};'.format(
    T=type,
    S=ssid,
    P=passwd,
    H=hidden
)
filename = 'SSID.'+ssid+'.QR.png'
img = qrcode.make(qr_string)
img.save('./'+filename)

#
# Generate HTML page to view or print
#
CSS = '* { font-family: Helvetica Neue,Arial,sans-serif; }'
HTML = '''
<meta charset="UTF-8">
<html>
<head>
<title>{title}</title>
<style type="text/css">{style}</style>
</head>
<body> {body} </body>
</html>
'''

print(HTML.format(title=filename,
                  style=CSS,
                  body='<img src="./'+filename+'"/>'
                  )
      )

