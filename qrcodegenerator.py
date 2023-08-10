import os
import segno

#this should be separ
qrCodePath = './static/images/qrcode.svg'
#if not os.path.exists(qrCodePath):
#    img.save(qrCodePath)


qrcode = segno.make('https://www.linkedin.com/in/edertech/')
qrcode.save('./static/images/qrcode.svg', dark='#32598f')