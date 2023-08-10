"""
Generate a QR code image if it does not exist
"""

import os
import segno

qrCodePath = './static/images/qrcode.svg'
if not os.path.exists(qrCodePath):
    qrcode = segno.make('https://www.linkedin.com/in/edertech/')
    qrcode.save('./static/images/qrcode.svg', dark='#32598f')