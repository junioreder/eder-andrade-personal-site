"""
Generate a QR code image if it does not exist
"""

import os
import segno

QR_CODE_IMAGE_PATH = './static/images/qrcode.svg'

def generateQRCode():
    if not os.path.exists(QR_CODE_IMAGE_PATH):
        qrcode = segno.make('https://www.linkedin.com/in/edertech/')
        qrcode.save(QR_CODE_IMAGE_PATH, dark='#32598f')