#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Script to generate QRCodes for URLs:
#   ./qr_urls.py
# -----------------------------------------------------------------------------

import qrcode
from qrcode.image.styledpil import StyledPilImage
from PIL import Image

urls = {
    # { "name": "url",
    "QR_Codes" : "https://github.com/1homas/QR_Codes",
}


for name,url in urls.items() :

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    img = qr.make_image(image_factory=StyledPilImage,
                        embeded_image_path="./logo.png",
                       )
    img.save('./'+name+'.QR.png')
